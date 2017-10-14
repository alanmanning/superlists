from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.


class HomePageTest(TestCase):

	def test_root_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEquals(found.func, home_page)

	def test_home_page_view_returns_correct_html(self):
		response = self.client.get('/')
		# html = response.content.decode('utf8')
		# expected_html = render_to_string('home.html')
		# self.assertEqual(html,expected_html)
		self.assertTemplateUsed(response,'home.html')

	def test_can_save_a_POST_request(self):
		response = self.client.post('/',data={'item_text' : 'A new list item'})
		html = response.content.decode('utf8')
		self.assertIn('A new list item',html)
		self.assertTemplateUsed(response,'home.html')

