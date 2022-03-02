from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields= ['title','writter', 'position', 'location', 'job_summary', 'duties', 'qualification']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter work title'}),
            'writter' : forms.Select(attrs={'id':'myuser', 'value':'','class':'form-control', 'placeholder':'select your name'}),
            'position' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter position of worker'}),
            'location' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your location'}),
            'job_summary' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'E.g organizing paper work'}),
            'duties' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'E.g pin and arrange paper alphabetically'}),
            'qualification' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'E.g form 4 leaver and attended training'}),
        }


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields= ['title', 'position', 'location', 'job_summary', 'duties', 'qualification']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control',}),
            'position' : forms.TextInput(attrs={'class':'form-control',}),
            'location' : forms.TextInput(attrs={'class':'form-control',}),
            'job_summary' : forms.Textarea(attrs={'class':'form-control',}),
            'duties' : forms.Textarea(attrs={'class':'form-control',}),
            'qualification' : forms.Textarea(attrs={'class':'form-control',}),
        }