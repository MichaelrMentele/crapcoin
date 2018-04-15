from django.test import TestCase
from django.test import Client

from sauron.models import Request
from sauron.tests.factories import RequestFactory


class Sauron(TestCase):
    """ Testcases for the Sauron API """
    def setUp(self):
        self.client = Client()

    def test_index_with_no_requests(self):
        response = self.client.get('/sauron/requests/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(
            response,
            'No requests have been seen by the eye!'
        )

    def test_index_with_requests(self):
        for _ in range(0, 10):
            RequestFactory()

        response = self.client.get('/sauron/requests/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, '<ul>')

    def test_creating_request(self):
        self.client.post('/sauron/requests/')
        num_rows = Request.objects.all().count()
        self.assertEqual(num_rows, 1)
