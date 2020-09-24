from django.test import SimpleTestCase
from Cart import views
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('cart-detail')
        self.assertEquals(resolve(url).func, views.cart_detail)
