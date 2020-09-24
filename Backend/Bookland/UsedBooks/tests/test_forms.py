from django.test import SimpleTestCase
from UsedBooks.forms import CommentForm


class TestForms(SimpleTestCase):
    def test_comment_form_valid_data(self):
        form = CommentForm(data={
            'content': 'something'
        })
        self.assertTrue(form.is_valid())

    def test_comment_form_no_data(self):
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
