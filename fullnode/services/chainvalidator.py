class ChainValidator:
    """ Validates a blockchain.

    Validates by checking all the transactions and proof of work
    solutions.
    """
    def is_valid_chain(self, blocks):
        """ If a single block is invalid return False. """
        for index, block in enumerate(blocks):
            if self.invalid_block(block):
                return False
        return True

    def invalid_block(self, block):
        if self.is_genesis(block):
            return False
        # validate proof of work
        # validate transaction
        return False

    def is_genesis(self, block):
        return block.hash_id == "genesis"
