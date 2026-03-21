from django.db import models

# Create your models here.
class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("Applied", "applied"),
        ("Interview", "interview"),
        ("Rejected", "rejected"),
        ("Offer", "offer"),
    ]
    company_name = models.CharField(max_length=255)
    position_title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date_applied = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.position_title}"