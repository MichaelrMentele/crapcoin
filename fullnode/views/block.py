from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from fullnode.services import BlockChain, Gossip
from fullnode.forms import BlockCreateForm
from fullnode.models import Block


class BlockCreateView(View):
    def post(self, request):
        form = BlockCreateForm(request.POST)
        if form.is_valid():
            block = Block.objects.create(
                payee=form.data['payee'],
                payer=form.data['payer'],
                amount=form.data['amount'],
            )
            Gossip.all_about_it(block)
            return redirect('blockchain')
        else:
            return HttpResponse("Invalid form--did you include all fields?")

    def get(self, request):
        return render(request, 'block_create.html', {'form': BlockCreateForm})
