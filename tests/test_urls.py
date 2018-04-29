from django.urls import reverse, resolve
from django.test import TestCase


class TestUrlRouting(TestCase):
    def test_block_route(self):
        url = reverse('block_detail', args=["some_hash"])
        self.assertEqual(url, '/fullnode/block/some_hash')

        resolver = resolve('/fullnode/block/some_hash')
        self.assertEqual(resolver.view_name, 'block_detail')

    def test_blockchain_route(self):
        url = reverse('blockchain')
        self.assertEqual(url, '/fullnode/blockchain/')
        resolver = resolve('/fullnode/blockchain/')
        self.assertEqual(resolver.view_name, 'blockchain')
