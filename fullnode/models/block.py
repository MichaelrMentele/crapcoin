from django.db import models
import hashlib


class Block(models.Model):
    content = models.TextField()
    previous_hash = models.CharField(max_length=1024)
    nonce = models.CharField(max_length=1024)
    hash_id = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.hash_id = self.compute_hash_id()
        super().save(*args, **kwargs)

    def compute_hash_id(self):
        return self.hash(self.previous_hash, self.content, self.nonce)

    def hash(self, previous_hash, content, nonce):
        return hashlib.sha256(
            "{previous_hash}||{content}||{nonce}".format(
                previous_hash=previous_hash,
                content=content,
                nonce=nonce,
            ).encode('utf-8')
        ).hexdigest()

    def is_valid(self):
        """ Recurses through all past blocks and validates them.

        A block is valid if:
        1. all past transactions were valid
        2. all proof of work is valid
        """
