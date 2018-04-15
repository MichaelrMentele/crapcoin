from django.db import models


class Block(models.Model):
    content = models.TextField()
    previous_hash = models.CharField(max_length=1024)
    nonce = models.CharField(max_length=1024)
    hash_id = models.CharField(max_length=1024)
