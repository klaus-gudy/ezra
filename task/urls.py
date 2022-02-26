from django.urls import path
from .views import HomeView, JobDetailView, AddPostView, UpdatePostView, DeleteView
# from . import views

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('job_detail/<int:pk>', JobDetailView.as_view(), name='job_detail'),
    path('add_job/', AddPostView.as_view(), name='add_job'),
    path('update_job/<int:pk>', UpdatePostView.as_view(), name='update_job'),
    path('delete_job/<int:pk>', DeleteView.as_view(), name='delete_job'),
]