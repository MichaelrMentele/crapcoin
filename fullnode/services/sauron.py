from functools import wraps
import requests

from crapcoin.settings import SAURON_URL, IS_SAURON


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
        if not self.config.get('IS_SAURON') and self.config.get('SAURON_URL'):
            self.see(request, response)
        return response

    def see(self, request, response):
        content = {'request': request, 'response': response}
        url = self.config.get('SAURON_URL') + '/sauron/requests'
        print('Reporting to Sauron at %s!' % url)
        try:
            return requests.post(url, content)
        except requests.exceptions.ConnectionError:
            print('Failed to report to Sauron; could not connect!')
