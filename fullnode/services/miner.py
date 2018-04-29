class Miner:
    """ A proof-of-work miner """
    def __init__(
        self,
        block_model=None,
        chain_service=None,
        validator=None
    ):
        self.block_model = block_model
        self.chain_service = chain_service
        self.validator = validator

    def mine(self, block):
        """
        Finds a one use number aka nonce that hashes together with the
        previous hash and content of the current hash into a new hash that
        has the number of leading zeros equal to the DIFFICULTY attribute.
        """
        import random

        while True:
            nonce = random.random() * 2**256
            result = Block.hash(
                previous_hash=block.hash_id,
                nonce=nonce
            )
            if(self._is_pow_solution(result)):
                block = Block.objects.create(
                    previous_hash=self.head.hash_id,
                    nonce=nonce,
                )
                return block

    def _is_pow_solution(self, new_hash):
        """ Checks whether a new hash has the correct number of leading zeros """
        count = 0
        for c in new_hash:
            if c == '0':
                count += 1
                if count >= self.DIFFICULTY:
                    return True
            else:
                return False

    def _previous_block(self, block=None):
        block = block or self.head
        hash_id = block.previous_hash
        if not self.is_genesis(block):
            return Block.objects.get(hash_id=hash_id)
        else:
            return None
