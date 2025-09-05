import django
import time


def handle_task_1(task_id: str) -> None:
    django.setup()

    # import models in each function to prevent 
    # "django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet"
    from main.models import TaskResult
    task = TaskResult.objects.get(task_id=task_id)

    try:
        time.sleep(5)  # Simulate CPU work
        
        result = f'task_1: {task.task_arg}'

        task.status = 'done'
        task.result = {'value': result}
        task.save()
    except Exception as e:
        task.status = 'failed'
        task.result = {'error': str(e)}
        task.save()

def handle_task_2(task_id):
    django.setup()

    from main.models import TaskResult
    task = TaskResult.objects.get(task_id=task_id)

    try:
        time.sleep(5)  # Simulate CPU work
        
        result = f'task_2: {task.task_arg}'

        task.status = 'done'
        task.result = {'value': result}
        task.save()
    except Exception as e:
        task.status = 'failed'
        task.result = {'error': str(e)}
        task.save()

def handle_task_3(task_id):
    django.setup()

    from main.models import TaskResult
    task = TaskResult.objects.get(task_id=task_id)

    try:
        time.sleep(5)  # Simulate CPU work
        
        result = f'task_3: {task.task_arg}'

        task.status = 'done'
        task.result = {'value': result}
        task.save()
    except Exception as e:
        task.status = 'failed'
        task.result = {'error': str(e)}
        task.save()

def handle_unknown_task(task_id):
    django.setup()

    from main.models import TaskResult
    task = TaskResult.objects.get(task_id=task_id)
    
    try:
        time.sleep(5)  # Simulate CPU work
        
        result = f'unknown_task: {task.task_arg}'

        task.status = 'done'
        task.result = {'value': result}
        task.save()
    except Exception as e:
        task.status = 'failed'
        task.result = {'error': str(e)}
        task.save()

def get_current_time():
    return '[' + time.strftime('%Y/%m/%d %H:%M:%S') + ']'
