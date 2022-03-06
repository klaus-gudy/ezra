from django.urls import path, include
from . import views

urlpatterns = [
    path('job/add', views.add_job, name='add_job'),

]