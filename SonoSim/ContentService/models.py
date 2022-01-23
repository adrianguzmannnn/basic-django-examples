"""This file contains the models for the object-relational mapper for the Content Service."""
import uuid
from django.db import models

class Patient(models.Model):
    """A table to store patient information."""
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    # pk: Django creates an auto-incrementing integer primary key by default.
    case_uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    volume_filename = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    age = models.PositiveIntegerField()
    case_history = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk}: {self.case_uuid}"
