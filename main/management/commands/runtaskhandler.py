from django.core.management.base import BaseCommand
import multiprocessing as mp 
import time

# importing models here is fine 
from main.models import TaskResult

# From Python documentation:
# "Raises RuntimeError if the start method has already been set and force is not True."
# "The default start method will change away from fork in Python 3.14."
# set force=True, in case if the start method has already been set
mp.set_start_method('spawn', force=True)

from ._private import (
    handle_task_1,
    handle_task_2,
    handle_task_3,
    handle_unknown_task,
    get_current_time
)

MAX_CONCURRENT_TASKS = 5
CHECK_INTERVAL = 20


class Command(BaseCommand):
    help = 'Run background task handler'

    def handle(self, *args, **kwargs):

        print(f'{get_current_time()} Starting task handler. Press Ctrl+C to stop.')

        try:
            while True:
                # active_children will join any processes which have already finished
                if len(mp.active_children()) < MAX_CONCURRENT_TASKS:
                    task = TaskResult.objects.filter(status='pending').first()
                    if task:
                        print(f'{get_current_time()} Starting task {task.task_id}')
                        task.status = 'running'
                        task.save()

                        task_id = task.task_id

                        match task.task_name:
                            case 'task_1':
                                # pass task.task_id, instead of the "task" object
                                # otherwise this will cause:
                                # "django.core.exceptions.AppRegistryNotReady: 
                                # Models aren't loaded yet."
                                # when using with multiprocessing
                                p = mp.Process(target=handle_task_1, args=(task_id,))
                                p.start()
                            case 'task_2':
                                p = mp.Process(target=handle_task_2, args=(task_id,))
                                p.start()
                            case 'task_3':
                                p = mp.Process(target=handle_task_3, args=(task_id,))
                                p.start()
                            case _:
                                # any unknown task
                                p = mp.Process(target=handle_unknown_task, args=(task_id,))
                                p.start()
                    else:
                        # No pending tasks
                        time.sleep(CHECK_INTERVAL)
                else:
                    # No available resources
                    time.sleep(CHECK_INTERVAL)
        except KeyboardInterrupt:  
            # go to the next line after ^C
            print('')
            # for those "running" tasks
            # set the status to "pending", so that they could be handled next time
            for task in TaskResult.objects.filter(status='running'):
                print(f'{get_current_time()} Halting task {task.task_id}')
                task.status = 'pending'
                task.save()
            print(f'{get_current_time()} Shutting down.')
