from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from fullnode.services import BlockChain, Gossip
from fullnode.forms import BlockCreateForm
from fullnode.models import Block


class BlockView(View):
    def get(self, request, hash_id):
        block = Block.objects.get(hash_id=hash_id)
        return render(request, 'block.html', {'crap_block': block})

    def post(self, request):
        import ipdb; ipdb.set_trace()


class BlockCreateView(View):
    def post(self, request):
        """ Used for internal transactions where this node creates a
        transaction. """
        form = BlockCreateForm(request.POST)
        if form.is_valid():
            block = Block(
                payee=form.data['payee'],
                payer=form.data['payer'],
                amount=form.data['amount'],
            )
        try:
            chain = BlockChain().add_block(block)
            Gossip.all_about_it(chain)
            return redirect('blockchain')
        except ValueError:
            return HttpResponse("Invalid form--did you include all fields?")

    def get(self, request):
        return render(request, 'block_create.html', {'form': BlockCreateForm})
