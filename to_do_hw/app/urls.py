from django.urls import path, re_path
from . import views

urlpatterns = [
    # Главная страница со списком задач
    path('', views.index, name='task_list'),
    path('task_filter', views.task_filter, name='task_filter'),
    # Данные о конкретной задаче
    # re_path(r'^task/(?P<task_id>\d+)/$', views.task_detail, name='task_detail'),
    # # Создание новой задачи
    # path('task/new/', views.task_create, name='task_create'),
    # # Редактирование задачи по ID
    # re_path(r'^task/(?P<task_id>\d+)/edit/$', views.task_edit, name='task_edit'),
    # # Удаление задачи по ID
    # re_path(r'^task/(?P<task_id>\d+)/delete/$', views.task_delete, name='task_delete')

]
