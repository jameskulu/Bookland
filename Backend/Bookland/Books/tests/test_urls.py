from django.test import SimpleTestCase
from Books import views
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, views.index)

    def test_detail_url_is_resolved(self):
        url = reverse('product-detail', args=[1])
        self.assertEquals(resolve(url).func, views.product_detail)

    def test_category_url_is_resolved(self):
        url = reverse('category', args=['slug'])
        self.assertEquals(resolve(url).func, views.categoryView)

    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, views.search)

    def test_wishlist_url_is_resolved(self):
        url = reverse('wishlist', args=[1])
        self.assertEquals(resolve(url).func, views.wishlist)
