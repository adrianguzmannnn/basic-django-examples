from django.db import models


class Visitor(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    ip = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.ip
