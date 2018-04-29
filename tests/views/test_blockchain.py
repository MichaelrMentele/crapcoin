from django.test import TestCase
from fullnode.services import BlockChain
from tests.factories import BlockFactory, BlockChainFactory


class TestBlockView(TestCase):
    def test_block_view(self):
        block = BlockFactory()
        response = self.client.get(f'/block/{block.hash_id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'block.html')
        self.assertContains(response, block.hash_id)


class TestBlockChainAPI(TestCase):
    def test_blockchain_view(self):
        with self.subTest("No blocks exist"):
            response = self.client.get('/blockchain')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'blockchain.html')
            self.assertContains(response, "This must be a crap coin...")

        with self.subTest("With many blocks, can view as a list"):
            chain = BlockChain()
            response = self.client.get('/blockchain')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'blockchain.html')
            self.assertContains(response, chain.head.hash_id)

    def test_blockchain_update(self):
        raise

    def test_can_tell_node_info(self):
        raise

    def test_user_can_create_block_transaction(self):
        raise
