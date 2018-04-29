from django.test import TestCase


class Node(TestCase):
    def test_attributes(self):
        with self.subTest('Has a name, which is a public key'):
            raise("Not implemented")

        with self.subTest('Has a port'):
            raise("Not implemented")

    def test_types(self):
        with self.subTest('Can be seed node'):
            raise

        with self.subTest('Can be fullnode'):
            raise

        with self.subTest('Can be sauron node'):
            raise
