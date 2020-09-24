from django.test import SimpleTestCase
from UsedBooks import views
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('used-books')
        self.assertEquals(resolve(url).func, views.used_books)

    def test_detail_url_is_resolved(self):
        url = reverse('used-books-detail', args=[1])
        self.assertEquals(resolve(url).func, views.used_books_detail)

    def test_category_url_is_resolved(self):
        url = reverse('used-books-category', args=['slug'])
        self.assertEquals(resolve(url).func, views.used_categoryView)

    def test_search_url_is_resolved(self):
        url = reverse('used-search')
        self.assertEquals(resolve(url).func, views.used_search)

    def test_listed_book_url_is_resolved(self):
        url = reverse('listed-books')
        self.assertEquals(resolve(url).func, views.listed_books)

    def test_book_post_url_is_resolved(self):
        url = reverse('book-post')
        self.assertEquals(resolve(url).func, views.book_post)
