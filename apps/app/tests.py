from django.test import TestCase

from app.views import index

class TestView(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
