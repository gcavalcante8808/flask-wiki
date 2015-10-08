import unittest
from flask_wiki.frontend.frontend import app


class FrontEndTestCase(unittest.TestCase):
    """
    Test All Wiki pages and features.
    """
    def setUp(self):
        self.client = app.test_client()

    def test_index_access(self):
        request = self.client.get('/')
        assert 'Home' in str(request.data)

    def test_create_new_page(self):
        pass
