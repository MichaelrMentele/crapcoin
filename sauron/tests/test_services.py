import json

from django.test import TestCase
from django.http import JsonResponse
import vcr
from sauron.services import all_seeing_eye, AllSeeingEye


class AllSeeingEyeTest(TestCase):
    def setUp(self):
        self.path = 'localhost:8000/sauron/requests/'

    @vcr.use_cassette('sauron/tests/cassettes/test_all_seeing_eye_can_see')
    def test_all_seeing_eye_can_see(self):
        f = lambda: JsonResponse({'ttl': 1, 'uuid': 'some_string', 'gossip': 'some gossip'})
        some_view = all_seeing_eye(f, config={'path': self.path})
        view_response = some_view()
        self.assertEqual(view_response.status_code, 200)

    @vcr.use_cassette('sauron/tests/cassettes/test_sauron_sees')
    def test_seeing(self):
        eye = AllSeeingEye(config={'path': self.path})
        response = eye.see('some content')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Seen by the Eye",
            json.loads(response.content)['message']
        )
