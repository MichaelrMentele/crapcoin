""" The methods in this module represent behaviors for the conceptual object,
a blockchain, that manages linking blocks together."""
from fullnode.models import Block
from fullnode.services.chainvalidator import ChainValidator


class BlockChain:
    def __init__(
        self,
        block_model=Block,
        validator=ChainValidator,
        miner=None,
        payee=None,
    ):
        self.block_model = block_model
        self.validator = validator()
        #self.miner = miner()

    def genesis(self, payee):
        return self.block_model.objects.create(
            payee=payee,
            **self.block_model.genesis_data(),
        )

    def fork_choice(self, new_chain):
        """ Replace or ignore this new blockchain.

        If the suggested blockchain is longer and valid. Delete the current
        chain and install the new chain.

        Otherwise raise a ValueError exception.

        Args:
            new_chain (list[DeserializedObject..]): Deserialized blocks.

        Returns:
            blockchain (Queryset): Blocks in the blockchain ordered by number.
        """
        blocks = [b.object for b in new_chain]
        blocks.sort(key=lambda block: block.number)
        if (len(blocks) > Block.objects.count() and self.validator.is_valid_chain(blocks)):
            Block.objects.all().delete()
            for block in blocks:
                block.save()
        return Block.objects.all()

    def add_block(self, block):
        if self.block_model.objects.count() == 0:
            self.genesis(block.payee)
        #self.validator.validate_block()
        block.previous_hash = self.last().hash_id
        block.save()

        return self.block_model.objects.all()

    def mint(self, **block_fields):
        """ Mines a new block and adds it to the chain. """
        previous_hash = self.block_model.objects.order_by('-number').first()
        block = Block(previous_hash=previous_hash, **block_fields)
        chain = self.minder.mine(block)
        return chain

    def difficulty(self):
        """ Currently, this returns the required number of leading zeros for
        proof of work.

        At the moment it is static, but in the future it could use the block
        time of the prior block for computing a new difficulty.
        """
        return 2

    def last(self):
        return self.block_model.objects.order_by('-created_at')[0]
