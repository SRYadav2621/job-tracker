from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company', 'role', 'job_url', 'applied_date', 'status', 'notes']
        widgets = {
            'company': forms.TextInput(attrs={'placeholder': 'e.g. Infosys'}),
            'role': forms.TextInput(attrs={'placeholder': 'e.g. Python Developer'}),
            'job_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
            'applied_date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Recruiter details, next steps, etc.'}),
        }
