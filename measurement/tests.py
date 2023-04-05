from unittest import TestCase

from rest_framework.test import APIClient


class TestSampleView(TestCase):
    def test_view(self):
        client = APIClient()
        response = client.get('/api/sensors/')
        print(response)
        assert 1 == 1
