from flask.ext.testing import TestCase
from flask_wiki.backend.backend import app, db


#TODO: Implement url_for based http ops.
#TODO: Try to use mixer to mock the tests.
class BackendTestCase(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all()

        from flask_wiki.backend.models import Page
        self.page = Page()
        self.page.name = 'MainPage'
        self.page.path = '/'

        db.session.add(self.page)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_list_of_pages(self):
        response = self.client.get('/pages-list')
        self.assertIn(self.page.name, str(response.data))
