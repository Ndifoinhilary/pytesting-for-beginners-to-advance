from django.db import models


# Create your models here.


class Company(models.Model):
    HIRING_STATUS = (
        ("LAYOFFS", "Layoffs"),
        ("HIRING", "Hiring"),
        ("HIRING_FREEZE", "Hiring Freeze"),
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=HIRING_STATUS, default="HIRING")
    last_update = models.DateTimeField(auto_now=True)
    application_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
