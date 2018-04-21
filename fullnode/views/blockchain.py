from django.shortcuts import render
from django.views import View

from fullnode.models import Block


class BlockView(View):
    def get(self, request, hash_id):
        block = Block.objects.get(hash_id=hash_id)
        return render(request, 'block.html', {'block': block})


class BlockChainView(View):
    def get(self, request):
        blocks = Block.objects.all().order_by('-created_at')
        return render(request, 'blockchain.html', {'chain': blocks})
