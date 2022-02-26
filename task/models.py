from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

STATUS = (
    (0,"undone"),
    (1,"done")
)

class Job(models.Model):
    title = models.CharField(max_length=200)
    writter = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_summary = models.TextField()
    duties = models.TextField(null=True, blank=False)
    qualification = models.TextField(null=True, blank=False)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.position + ' | ' + str(self.writter)

    def get_absolute_url(self):
        # return reverse('job_detail', args=(str(self.id)))
        return reverse('home')
