import unittest
import os
import tempfile
from src import wiki


class WikiTestCase(unittest.TestCase):
    """
    Test All Wiki pages and features.
    """

    def setUp(self):
        # For Now, creates a temporary Database.
        self.db_fd, wiki.app.config['DATABASE'] = tempfile.mkstemp()
        wiki.app.config['TESTING'] = True
        wiki.init_db(wiki.db)
        self.app = wiki.app.test_client()

    def tearDown(self):
        # For now, unlink the temp db created.
        os.close(self.db_fd)
        os.unlink(wiki.app.config['DATABASE'])

    def test_index_access(self):
        request = self.app.get('/')
        assert 'Home' in str(request.data)

if __name__ == '__main__':
    unittest.main()