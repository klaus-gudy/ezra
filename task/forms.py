from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields= ['title','company', 'location','description', 'qualification', 'job_type']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter work title'}),
            'company' : forms.TextInput(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your location'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'E.g organizing paper work'}),
            'qualification' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g form 4 leaver and attended training'}),
            'job_type' : forms.TextInput(attrs={'class':'form-control'}),
        }


class JobUpdateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields= ['title','company', 'location','description', 'qualification', 'job_type']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter work title'}),
            'company' : forms.TextInput(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your location'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'E.g organizing paper work'}),
            'qualification' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'E.g form 4 leaver and attended training'}),
            'job_type' : forms.TextInput(attrs={'class':'form-control'}),
        }