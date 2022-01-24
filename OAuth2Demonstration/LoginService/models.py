"""This file contains the models for the object-relational mapper for the Login Service."""
from django.db import models

class User(models.Model):
    """A table to store user information."""

    # pk: Django creates an auto-incrementing integer primary key by default.
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    expected_token = models.TextField()

    def __str__(self):
        return f"{self.username}"
