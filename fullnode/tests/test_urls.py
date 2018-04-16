from django.urls import reverse, resolve
from django.tests import TestCase


class TestUrlRouting(TestCase):
    def test_block_route(self):
        url = reverse('block', args=["some_hash"])
        self.assertEqual(url, '/block/some_hash/')

        resolver = resolve('/block/some_hash')
        self.assertEqual(resolver.view_name, 'block')

    def test_blockchain_route(self):
        url = reverse('blockchain')
        self.assertEqual(url, '/blockchain/')

        resolver = resolve('/blockchain/')
        self.assertEqual(resolver.view_name, 'blockchain')
