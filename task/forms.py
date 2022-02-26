from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields= ['title','writter', 'position', 'location', 'job_summary', 'duties', 'qualification']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'writter' : forms.Select(attrs={'id':'myuser', 'value':''}),
            'position' : forms.TextInput(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
            'job_summary' : forms.Textarea(attrs={'class':'form-control'}),
            'duties' : forms.Textarea(attrs={'class':'form-control'}),
            'qualification' : forms.Textarea(attrs={'class':'form-control'}),
        }