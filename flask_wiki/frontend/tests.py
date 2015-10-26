from flask import url_for
from xvfbwrapper import Xvfb
from flask.ext.testing import LiveServerTestCase
from selenium import webdriver
from flask_wiki.frontend.frontend import app


class FrontendTestCase(LiveServerTestCase):
    """
    Test frontend access through firefox webdriver
    """
    def create_app(self):
        return app

    def setUp(self):
        self.xvfb = Xvfb(width=1024,height=768)
        self.xvfb.start()
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        self.xvfb.stop()

    def test_index_access(self):
        """
        Try to Access the first page.
        :return:
        """
        url = self.get_server_url()
        print(url)
        self.browser.get(url)

        self.assertIn('Home', self.browser.title)
