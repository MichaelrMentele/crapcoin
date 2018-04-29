from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from fullnode.models import Peer


class PeerApi(View):
    def get(self, request):
        peers = Peer.objects.all()
        return JsonResponse(serializers.serialize('json', peers), safe=False)

    def post(self, request):
        print("creating peer...")
        port = int(request.body.decode().split('=')[1])
        Peer.objects.get_or_create(port=port)
        return HttpResponse(status=200)


class PeerView(View):
    def get(self, request):
        peers = Peer.objects.all()
        return render(request, 'peers.html', {'peers': peers})
