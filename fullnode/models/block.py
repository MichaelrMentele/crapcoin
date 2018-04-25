from django.db import models
import hashlib


class Block(models.Model):
    # Transaction data
    payer = models.CharField(max_length=1024)
    payee = models.CharField(max_length=1024)
    amount = models.IntegerField()
    signature = models.CharField(max_length=1024)

    # Block data
    number = models.IntegerField()
    previous_hash = models.CharField(max_length=1024)
    nonce = models.CharField(max_length=1024)
    hash_id = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.number = 1
        self.hash_id = self.compute_hash_id()
        super().save(*args, **kwargs)

    def compute_hash_id(self):
        txn = self.hash(self.payer, self.payee, self.amount, self.signature)
        return self.hash(self.previous_hash, txn, self.nonce)

    def hash(self, *args):
        hashables = [arg.encode('utf-8') for arg in args]
        return hashlib.sha256(b"||".join(hashables)).hexdigest()

    def is_valid(self):
        """ Recurses through all past blocks and validates them.

        A block is valid if:
        1. all past transactions were valid
        2. all proof of work is valid
        """
        pass
