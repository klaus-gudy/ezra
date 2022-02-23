from django.contrib import admin
from .models import Job

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'job_summary']
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(Job, PostAdmin)