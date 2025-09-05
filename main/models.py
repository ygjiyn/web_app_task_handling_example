from django.db import models


class TaskResult(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('done', 'Done'),
        ('failed', 'Failed'),
    ]

    TASK_NAME_CHOICES = [
        ('task_1', 'Task 1'),
        ('task_2', 'Task 2'),
        ('task_3', 'Task 3'),
        ('unknown_task', 'Unknown Task'),
    ]

    task_id = models.CharField(max_length=64, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # no need to set blank=True when handling the POST request manually
    # set null=True to allow this field to be NULL in the database 
    # null=False is the default value, in this case, default is required
    result = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # the handler could handle multiple tasks
    # one task_name corresponds to one function handling this task
    task_name = models.CharField(choices=TASK_NAME_CHOICES, default='unknown-task')
    task_arg = models.JSONField(null=True)
