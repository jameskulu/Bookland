from django.test import TestCase, Client
from django.urls import resolve, reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('cart-detail')

    def test_index_list_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Cart/cart_detail.html')
