
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job

from .forms import JobForm, JobUpdateForm

from django.urls import reverse_lazy

# @login_required(login_url='login')
# def home(request):
#     return render(request, 'task/home.html')


class HomeView(ListView):
    model = Job
    template_name = 'task/home.html'
    ordering = ['-created_on']

class JobDetailView(DetailView):
    model = Job
    template_name = 'task/job_detail.html'

class AddPostView(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'task/add_job.html'

class UpdatePostView(UpdateView):
    model = Job
    form_class = JobUpdateForm
    # fields= ['title', 'position', 'location', 'job_summary', 'duties', 'qualification']
    template_name = 'task/update_job.html'

class DeleteView(DeleteView):
    model = Job
    template_name = 'task/delete_job.html'
    success_url = reverse_lazy('home')

