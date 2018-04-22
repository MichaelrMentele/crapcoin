from django.views import View
from django.http import JsonResponse

from fullnode.models import Peer


class PeerView(View):
    def get(self, request):
        peers = Peer.objects.all()
        return JsonResponse({'peers': peers})
