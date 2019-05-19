
from todoapp import views
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('', views.Dashboard.as_view(), name='index'),
    url('get_todo_list', views.gettodolist, name='get_todo_list')
]