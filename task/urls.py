from django.urls import path
from .views import HomeView, JobDetailView, AddPostView
# from . import views

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('job_detail/<int:pk>', JobDetailView.as_view(), name='job_detail'),
    path('add_job/', AddPostView.as_view(), name='add_job'),
]