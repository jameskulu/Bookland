from django.test import TestCase, Client
from Books import views
from Books import models
from django.urls import resolve, reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')

    def test_index_list_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Books/index.html')
