""" A service that bootstraps a new node into the network """
import requests
import random
from django.core import serializers
from fullnode.models import Peer
from crapcoin.settings import TRACKER_URL, IS_TRACKER
import logging

logger = logging.getLogger(__name__)


class Bootstrapper:
    """ Middleware that asks for peers from the tracker if none exist """
    def __init__(self, get_response, config=None):
        self.get_response = get_response

    def __call__(self, request, *params, **kwargs):
        response = self.get_response(request, *params, **kwargs)
        logger.info("Bootstrapping...")
        if Peer.objects.count() == 0 and not IS_TRACKER:
            self.bootstrap(request)
        return response

    def bootstrap(self, request):
        response = requests.get(TRACKER_URL + '/api/peer')
        current_node_port = int(request.META['SERVER_PORT'])
        deserialized = serializers.deserialize('json', response.json())
        for serial_object in deserialized:
            if serial_object.object.port != current_node_port:
                serial_object.object.save()
        logger.info('Fetched and stored peers from the tracker.')

        requests.post(
            'http://localhost:8999/api/peer/create',
            {'port': current_node_port}
        )
