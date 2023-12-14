from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Indexes into author's table which currently is part of django default USER model
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    last_modified_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title