from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    # Stock authentication URL mappings
    path('accounts/', include('django.contrib.auth.urls')),
    path('todo/list', views.todo_list, name='todolist'),
    path('todo/create', views.todo_create, name='todocreate')
]