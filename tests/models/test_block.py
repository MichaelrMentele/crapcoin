from django.test import TestCase
tests.factories import BlockFactory


class TestBlock(TestCase):
    def test_block_has_attributes(self):
        with self.subTest("Has the content field"):
            raise("Not implemented")

        with self.subTest("Has the previous_hash field"):
            raise

        with self.subTest("Has the nonce field"):
            raise

        with self.subTest("Has a hash_id field"):
            raise

    def test_is_valid_block(self):
        raise

    def test_computes_hash_id_on_save(self):
        block = BlockFactory()
        self.assertTrue(block.hash_id)
