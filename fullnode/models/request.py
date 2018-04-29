from django.db import models


class Request(models.Model):
    body = models.TextField()
    host = models.CharField(max_length=80)
    method = models.CharField(max_length=10)
    uri = models.CharField(max_length=100)
    port = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Response(models.Model):
    content = models.TextField()
    status_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
