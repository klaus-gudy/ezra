from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
User = get_user_model()

CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Remote', 'Remote'),
)

class Job(models.Model):
    owner = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    qualification = models.CharField(max_length=200)
    job_type = models.CharField(max_length=30, choices=CHOICES, default='Full Time', null=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Applicant(models.Model):
    job = models.ForeignKey(Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant


class Selected(models.Model):
    job = models.ForeignKey(Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant