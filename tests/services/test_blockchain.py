from django.test import TestCase
from faker import Faker
from fullnode.models import Block
from fullnode.services import BlockChain


class TestBlockChain(TestCase):
    """ Wraps the stored blocks and provides management for chaining """
    def test_init(self):
        with self.subTest("An empty new chain creates a genesis block"):
            self.assertEqual(Block.objects.count(), 0)
            self.assertEqual(BlockChain().head, Block.objects.first())
            self.assertEqual(Block.objects.count(), 1)

        with self.subTest("An existing chain doesn't create more blocks"):
            BlockChain()
            self.assertEqual(Block.objects.count(), 1)
            BlockChain()
            self.assertEqual(Block.objects.count(), 1)

    def test_mint(self):
        with self.subTest("Can mine new blocks"):
            transaction = Faker().sha256()
            BlockChain().mint(transaction)
            self.assertEqual(Block.objects.count(), 2)

    def test_is_valid_block(self):
        with self.subTest("True with valid pow solution"):
            chain = BlockChain()
            transaction = Faker().sha256()
            new_block = chain.mint(transaction)
            chain.is_valid_block(new_block)

        with self.subTest("False with invalid pow solution"):
            chain = BlockChain()
            self.assertEqual(chain.is_valid_pow("fake_hash"))

        with self.subTest("True if transaction output <= input"):
            raise

        with self.subTest("False if transaction output > input"):
            raise

        with self.subTest("False if doublespend"):
            raise

    def test_does_not_allow_negative_balances(self):
        raise

    def test_forks_on_longer_valid_chain(self):
        raise


class TestTransaction(TestCase):
    """ A transaction is one-to-one with a block in CrapCoin """
    def test_has_from_and_to_pks(self):
        raise

    def test_has_amount(self):
        raise

    def test_has_signature(self):
        raise

    def test_validates(self):
        with self.subTest("Sender has coins"):
            raise

        with self.subTest("Catches double spends"):
            raise

    def test_sends_remainder_back_to_self(self):
        raise


class TestMiningAgent(TestCase):
    """ Mines blocks and tells it's fullnode when it has a new block. """
