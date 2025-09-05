from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('result/<str:task_id>/', views.result_details, name='result_details'),
    path('status/', views.status, name='status'),
    path('submit-1/', views.submit_1, name='submit_1'),
    path('submit-2/', views.submit_2, name='submit_2'),
    path('submit-3/', views.submit_3, name='submit_3'),
    path('api/get_task_result_by_id/<str:task_id>/', views.api_get_task_result_by_id, name='api_get_task_result_by_id'),
]
