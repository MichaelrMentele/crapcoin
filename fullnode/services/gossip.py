import requests
from fullnode.models import Peer
from django.core import serializers
import logging


logger = logging.getLogger(__name__)


class Gossip:
    @classmethod
    def all_about_it(cls, news):
        peers = Peer.objects.all()
        pickles = serializers.serialize('json', news)

        logger.info("Telling my peers about it...")
        for peer in peers:
            try:
                requests.post(
                    f'http://localhost:{peer.port}/blockchain/update',
                    pickles
                )
            except:
                logger.info(f"{peer.port} isn't responding, deleting from peer list")
                peer.delete()
