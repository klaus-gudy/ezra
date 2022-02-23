from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView
from .models import Job

# @login_required(login_url='login')
# def home(request):
#     return render(request, 'task/home.html')


class HomeView(ListView):
    model = Job
    template_name = 'task/home.html'

class JobDetailView(DetailView):
    model = Job
    template_name = 'task/job_detail.html'

class AddPostView(CreateView):
    model = Job
    fields= ['title','position', 'location', 'job_summary', 'duties', 'qualification']
    # fields='__all__'
    template_name = 'task/add_job.html'