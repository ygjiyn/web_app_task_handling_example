from django.contrib import admin

# Register your models here.

from .models import TaskResult

admin.site.register(TaskResult)
