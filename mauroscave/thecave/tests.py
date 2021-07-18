from django.test import TestCase
from selenium import webdriver


class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Safari()

    def test_there_is_homepage(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Mauricio Diaz', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()


class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'thecave/home.html')
