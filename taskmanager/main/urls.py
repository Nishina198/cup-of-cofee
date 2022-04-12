
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='home'),
     path('about-me', views.about, name='sale'),
     path('my-task', views.task, name='task'),
]