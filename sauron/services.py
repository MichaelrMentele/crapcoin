from functools import wraps
import requests


def all_seeing_eye(func, config=None):
    """
    Publishes to Sauron log aggregator.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        response = func(*args, **kwargs)
        AllSeeingEye(config=config).see(request, response)
        return response
    return wrapper


class AllSeeingEye(object):
    """ Can be used as a middleware or decorator to report to sauron """
    def __init__(self, get_response=None, config=None):
        self.get_response = get_response
        self.config = config or {}

    def __call__(self, request):
        response = self.get_response(request)
        self.see(request, response)
        return response

    def see(self, request, response):
        content = {'request': request, 'response': response}
        url = 'http://%s' % self.config.get('path')
        print('Reporting to Sauron at %s!' % url)
        return requests.post(url, content)
