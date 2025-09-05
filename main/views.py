from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from uuid import uuid4

from .models import TaskResult
from .management.commands.runtaskhandler import MAX_CONCURRENT_TASKS

import json


def home(request):
    return render(request, 'main/home.html', {'navbar_select': 'home'})

def result(request: HttpRequest):
    if request.method == 'POST':
        task_id = request.POST.get('taskId', None)
        return HttpResponseRedirect(reverse('main:result_details', args=(task_id,)))
    else:
        return render(request, 'main/result.html', {'navbar_select': 'result'})

def result_details(request: HttpRequest, task_id: str):
    task = TaskResult.objects.get(task_id=task_id)
    return render(request, 'main/result-details.html', {
        'navbar_select': 'result', 
        'task_id': task.task_id,
        'created_at': task.created_at,
        'status': task.status
    })

def status(request):
    return render(request, 'main/status.html', {'navbar_select': 'status'})

def submit_1(request: HttpRequest):
    if request.method == 'POST':
        field1 = request.POST.get('field1', None)
        field2 = request.POST.get('field2', None)
        task = TaskResult()
        task.task_id = str(uuid4())
        task.task_name = 'task_1'
        task.task_arg = {'field1': field1, 'field2': field2}
        task.save()
        return HttpResponseRedirect(reverse('main:result_details', args=(task.task_id,)))
    else:
        return render(request, 'main/submit-1.html', {'navbar_select': 'submit'})

def submit_2(request):
    return render(request, 'main/submit-2.html', {'navbar_select': 'submit'})

def submit_3(request):
    return render(request, 'main/submit-3.html', {'navbar_select': 'submit'})

def api_get_task_result_by_id(request: HttpRequest, task_id: str):
    task = TaskResult.objects.get(task_id=task_id)
    return JsonResponse({'result': json.dumps(task.result), 'status': task.status})
