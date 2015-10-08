import unittest
from flask import url_for
import os
import tempfile
from src.backend.backend import app


class BackendTestCase(unittest.TestCase):
    def setUp(self):
        # For Now, creates a temporary Database.
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        # For now, unlink the temp db created.
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_get_list_of_pages(self):
        request = self.app.get(url_for('pages'))
        self.assertEqual(request.status_code, 200)

if __name__ == '__main__':
    unittest.main()