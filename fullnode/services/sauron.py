from functools import wraps
import requests

from crapcoin.settings import SAURON_URL


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


class AllSeeingEye(object):
    """ Can be used as a middleware or decorator to report to sauron """
    def __init__(self, get_response, config=None):
        self.get_response = get_response
        self.config = config or {'SAURON_URL': SAURON_URL}

    def __call__(self, request, *params, **kwargs):
        response = self.get_response(request, *params, **kwargs)
        self.see(request, response)
        return response

    def see(self, request, response):
        content = {'request': request, 'response': response}
        if self.config.get('SAURON_URL'):
            url = 'http://%s' % self.config.get('SAURON_URL')
            print('Reporting to Sauron at %s!' % url)
            try:
                return requests.post(url, content)
            except Exception:
                print('Failed to report to Sauron; could not connect!')
        else:
            print('The eye is missing Sauron\'s url')
