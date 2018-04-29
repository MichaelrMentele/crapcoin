from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core import serializers

from fullnode.models import Block
from fullnode.services import BlockChain, Gossip


class BlockChainView(View):
    def get(self, request):
        blocks = Block.objects.all().order_by('-created_at')
        return render(
            request,
            'blockchain.html',
            {'chain': blocks, 'page_title': 'Chain Explorer'}
        )

    def unseen_chain(self, chain):
        current_head = BlockChain().last().hash_id
        new_chain_head = chain.order_by('-number').first().hash_id
        return current_head != new_chain_head

    def post(self, request):
        generator = serializers.deserialize('json', request.body)
        chain = [block for block in generator]
        chain_queryset = BlockChain().fork_choice(chain)
        if self.unseen_chain(chain_queryset):
            Gossip.all_about_it(chain)
            return HttpResponse("Accepted new blocks.", status=200)
        else:
            return HttpResponse("Rejected blocks. Chain has been seen.", status=202)
