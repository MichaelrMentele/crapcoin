from faker import Faker
from factory.django import DjangoModelFactory


class RequestFactory(DjangoModelFactory):
    class Meta:
        model = 'fullnode.Request'

    body = "fake request"
    created_at = Faker().date_time()
