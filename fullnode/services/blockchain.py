from fullnode.models import Block


class BlockChain():
    """ An ephemeral object that manages linked blocks """
    DIFFICULTY = 2

    def __init__(self):
        try:
            self.head = Block.objects.all().order_by('-created_at')[0]
        except IndexError:
            self.head = self._create_genesis_block()

    def mint(self, content):
        """ Mines a new block and adds it to the chain. """
        previous_hash = self.head.hash_id
        block = self._mine(content)

        self.head = block
        return block

    def is_valid_block(self, block):
        # get the heads hash_id
        # hash new block with nonce, check solution
        # if valid, self.head = new_block
        # save the new_block
        if Block.objects.exists(hash_id=block.hash_id):
            return True
        elif self.is_valid_block(head):
            self.validate_blockchain(self._previous_block(head))

        raise

    def is_genesis(self, block):
        return block.hash_id == "genesis"

    # PRIVATE

    def _mine(self, content):
        """
        Finds a one use number aka nonce that hashes together with the
        previous hash and content of the current hash into a new hash that
        has the number of leading zeros equal to the DIFFICULTY attribute.
        """
        import random

        while True:
            nonce = random.random() * 2**256
            result = self.head.hash(
                previous_hash=self.head.hash_id,
                content=content,
                nonce=nonce
            )
            if(self._is_pow_solution(result)):
                block = Block.objects.create(
                    previous_hash=self.head.hash_id,
                    content=content,
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

    def _create_genesis_block(self):
        return Block.objects.create(
            content="genesis",
            previous_hash="genesis",
            nonce="genesis"
        )


class Transaction:
    def __init__(self, sender_pk, reciever_pk, utxo, stxo):
        self.sender_pk = sender_pk
        self.reciever_pk = reciever_pk
        self.utxo = utxo
        self.stxo = stxo

    def hash_transaction(self):
        raise

    def validate(self):
        raise
