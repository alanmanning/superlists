from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from lists.models import Item
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_view_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_item_save_returns_redirect(self):
        response = self.client.post('/',data={'item_text' : 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],'/lists/a-unique-url')

    def test_saved_item_appears_on_page(self):
        response = self.client.post('/',data={'item_text' : 'A new list item'})
        response = self.client.get('/')
        self.assertIn('A new list item',response.content.decode())

class ItemModelTest(TestCase):

  def test_saving_and_retreiving_items(self):
      first_item = Item()
      first_item.text = 'The first ever list item'
      first_item.save()

      second_item = Item()
      second_item.text = 'Second list item'
      second_item.save()

      saved_items = Item.objects.all()
      self.assertEqual(saved_items.count(),2)

      self.assertEqual(saved_items[0].text,'The first ever list item')
      self.assertEqual(saved_items[1].text,'Second list item')


class ListViewTest(TestCase):

    def test_displays_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/a-unique-url/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')