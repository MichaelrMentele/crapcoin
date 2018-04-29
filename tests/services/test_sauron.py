import json

from mock import Mock
import vcr
from django.test import TestCase
from django.http import JsonResponse

from fullnode.services import all_seeing_eye, AllSeeingEye


class AllSeeingEyeDecoratorTest(TestCase):
    def setUp(self):
        self.path = 'localhost:8000/sauron/requests/'

    @vcr.use_cassette('sauron/tests/cassettes/test_all_seeing_eye_can_see')
    def test_all_seeing_eye_can_see(self):
        view = lambda request: JsonResponse({'ttl': 1, 'uuid': 'some_string', 'gossip': 'some gossip'})
        some_view = all_seeing_eye(view, config={'path': self.path})
        view_response = some_view("some_request")
        self.assertEqual(view_response.status_code, 200)

    @vcr.use_cassette('sauron/tests/cassettes/test_sauron_sees')
    def test_seeing(self):
        eye = AllSeeingEye(Mock(), config={'path': self.path})
        response = eye.see('some request', 'some response')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Seen by the Eye",
            json.loads(response.content)['message']
        )


class AllSeeingEyeMiddlewareTest(TestCase):
    def test_as_middleware(self):
        self.middleware = AllSeeingEye(Mock())
        self.middleware.see = Mock()
        self.request = Mock()
        self.request.META = {
                "REQUEST_METHOD": "POST",
                "HTTP_OPERATING_SYSTEM_VERSION": "ICE CREAM",
                "HTTP_PLATFORM": "ANDROID",
                "HTTP_APP_VERSION": "1.0.0",
                "HTTP_USER_AGENT": "AUTOMATED TEST"
        }
        self.request.path = '/testURL/'
        self.request.session = {}

        self.middleware(self.request)
        self.assertTrue(self.middleware.see.called)
