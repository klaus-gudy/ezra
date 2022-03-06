from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Applicant, Selected
# from candidate.models import Profile, Skill
from .forms import JobForm
from django.contrib.auth.decorators import login_required
# from django.conf import settings
# from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib import messages
# from django.views.generic import UpdateView

def add_job(request):
    user = request.user
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.owner = user
            data.save()
            return redirect('home')
    else:
        form = NewJobForm()
    context = {
        # 'add_job_page': "active",
        'form': form,
        # 'rec_navbar': 1,
    }
    return render(request, 'task/add_job.html', context)