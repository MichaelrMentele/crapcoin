from django.db import models


class Request(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
