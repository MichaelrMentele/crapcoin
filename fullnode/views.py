from django.shortcuts import render
from django.views import View


class BlockView(View):
    def get(self, request, hash_id):
        # get block with that hash id
        # render it via template
        pass


class BlockChainView(View):
    def get(self, request):
        # get all blocks
        # render them all via template
        pass
