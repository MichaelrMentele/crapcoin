from django import models


class Account(models.Model):
    public_key = models.CharField(max_length=1024)
    balance = models.IntegerField()
