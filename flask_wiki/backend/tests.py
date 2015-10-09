from flask.ext.testing import TestCase
from flask_wiki.backend.backend import app, db
from flask_wiki.backend.custom_serialization_fields import GUIDSerializationField
import uuid


#TODO: Implement url_for based http ops.
#TODO: Try to use mixer to mock the tests.
class BackendTestCase(TestCase):
    """
    Test all Backend API EndPoints.
    """
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        # Put the application in testing mode.
        app.config['TESTING'] = True
        return app

    def setUp(self):
        # Create a temp database and create an Page Object.
        db.create_all()

        from flask_wiki.backend.models import Page

        self.page = Page()
        self.page.guid = uuid.uuid4()
        self.page.name = 'MainPage'
        self.page.path = '/'

        db.session.add(self.page)
        db.session.commit()

    def tearDown(self):
        # Remove the temp database created.
        # db.session.remove()
        # db.drop_all()
        pass

    def test_get_list_of_pages(self):
        response = self.client.get('/pages-list')
        # Can we Find the Main Page in the response?
        self.assertIn(self.page.name, response.json[0].values())

        # Can we find a GUID key.
        self.assertIn('guid', response.json[0].keys())

        # The Guid is Valid?
        # Testing Customized Serialization Field
        result = GUIDSerializationField().deserialize(response.json[0]['guid'])
        self.assertTrue(result)
