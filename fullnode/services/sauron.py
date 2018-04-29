from functools import wraps
import requests
import json
import logging

from crapcoin.settings import SAURON_URL, IS_SAURON


logger = logging.getLogger(__name__)


def all_seeing_eye(func, config=None):
    """
    Publishes to Sauron log aggregator.
    """
    @wraps(func)
    def wrapper(*params, **kwargs):
        middleware = AllSeeingEye(func, config=config)
        response = middleware(*params)
        return response
    return wrapper


class AllSeeingEye:
    """ Can be used as a middleware or decorator to report to sauron """
    def __init__(self, get_response, config=None):
        self.get_response = get_response
        self.config = config or {'SAURON_URL': SAURON_URL,
                                 'IS_SAURON': IS_SAURON}

    def __call__(self, request, *params, **kwargs):
        response = self.get_response(request, *params, **kwargs)
        logger.info("Reporting too sauron...")
        logger.info(self.config)
        if not self.config.get('IS_SAURON') and self.config.get('SAURON_URL'):
            logger.info("In sauron")
            self.see(request, response)
        return response

    def see(self, request, response):
        request_data = {
            'body': request.body.decode('utf-8'),
            'uri': request.get_raw_uri(),
            'host': request.get_host(),
            'port': request.get_port(),
            'method': request.method,
        }
        response_data = {
            'content': response.content.decode('utf-8'),
            'status_code': response.status_code,
        }
        content = json.dumps({
            'request': request_data,
            'response': response_data,
        })
        url = self.config.get('SAURON_URL') + '/sauron/requests'
        logger.info('Reporting to Sauron at %s!' % url)
        try:
            return requests.post(url, content)
        except requests.exceptions.ConnectionError:
            logger.error('Failed to report to Sauron; could not connect!')
