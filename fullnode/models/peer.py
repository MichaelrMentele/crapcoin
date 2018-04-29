from django.db import models


class Peer(models.Model):
    """ A Peer is a node in the CrapCoin network. """
    port = models.IntegerField(unique=True)
    # TODO add public key / private key
    created_at = models.DateTimeField(auto_now_add=True)
    # TODO last_heard_from = models.DateTimeField()
