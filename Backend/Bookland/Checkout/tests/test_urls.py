from django.test import SimpleTestCase
from Checkout import views
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, views.checkout)
