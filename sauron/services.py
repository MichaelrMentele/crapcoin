from functools import wraps
import requests


def all_seeing_eye(func, config=None):
    """
    Publishes to Sauron log aggregator.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        AllSeeingEye(config=config).see(response)
        return response
    return wrapper


class AllSeeingEye(object):
    def __init__(self, config=None):
        self.config = config or {}

    def see(self, content):
        url = 'http://%s' % self.config.get('path')
        print('Reporting to Sauron at %s!' % url)
        return requests.post(url, content)
