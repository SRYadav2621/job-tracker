from django.conf import settings
from django.db import models

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'), ('ASSESSMENT', 'Assessment'),
        ('INTERVIEW', 'Interview'), ('OFFER', 'Offer'), ('REJECTED', 'Rejected'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='job_applications')
    company = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    job_url = models.URLField(blank=True)
    applied_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='APPLIED')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-applied_date', '-created_at']

    def __str__(self):
        return f'{self.role} at {self.company}'
