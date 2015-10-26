from xvfbwrapper import Xvfb
from selenium import webdriver
from flask.ext.testing import LiveServerTestCase
from flask_wiki.frontend.frontend import app


class FrontendTestCase(LiveServerTestCase):
    """
    Test frontend access through firefox webdriver
    """
    def create_app(self):
        return app

    def setUp(self):
        self.xvfb = Xvfb(width=1024, height=768)
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
        self.browser.get(url)

        # Can we see the right value on title bar?
        self.assertIn('Home', self.browser.title)

        # Can we find a specific page?
        self.browser.find_element_by_link_text('Find Page').click()

        self.assertIn('find-page', self.browser.current_url)

        self.fail('Implement Find Page.')
        self.browser.find_element_by_id('search-field').text('index')
        self.browser.find_element_by_link_text('Search').click()

        self.browser.find_elements_by_link_text('Index')
