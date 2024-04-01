from django.db import models
from django.contrib.contenttypes.models import ContentType


class AdminContext(models.Model):
    slug = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    models = models.ManyToManyField(ContentType)

    class Meta:
        indexes = [models.Index(fields=["name"])]

    def __str__(self):
        return self.name
