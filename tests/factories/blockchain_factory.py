from faker import Faker
from factory.django import DjangoModelFactory
from fullnode.models import Block
from fullnode.services import BlockChain


class BlockFactory(DjangoModelFactory):
    class Meta():
        model = Block

    content = Faker().sha256()
    previous_hash = Faker().sha256()
    nonce = Faker().sha256()


class BlockChainFactory(object):
    def __init__(self):
        chain = BlockChain()
        for _ in range(0, 10):
            content = Faker().sha256()
            chain.mint(content)
        return chain
