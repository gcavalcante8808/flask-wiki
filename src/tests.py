import unittest
import os
import tempfile
from flask.ext.sqlalchemy import SQLAlchemy
from src import wiki


class WikiTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, wiki.app.config['DATABASE'] = tempfile.mkstemp()
        wiki.app.config['TESTING'] = True
        wiki.init_db(wiki.db)
        self.app = wiki.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(wiki.app.config['DATABASE'])

    def test_rdbm_access(self):
        pass

if __name__ == '__main__':
    unittest.main()