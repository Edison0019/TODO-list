from django.contrib import admin
from django.urls import path
from .views import update_task,confirm,index

url_patterns = ([
    path('',index,name='home'),
    path('update/<str:pk>/',update_task,name='update'),
    path('confirm/<str:pk>/',confirm,name='confirmation'),
],'tasks')
