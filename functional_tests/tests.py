from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import unittest
import time
import pdb

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.PhantomJS()

	def tearDown(self):
		self.browser.quit()

	def wait_for_DOM_item(self,id):
		start_time = time.time()
		while True:
			try:
				DOM_item = self.browser.find_element_by_id(id)
				return DOM_item
			except (AssertionError, WebDriverException) as e:
					if time.time() - start_time > MAX_WAIT:
						raise e
					time.sleep(0.5)

	def check_row_in_list_table(self, row_text):
		table = self.wait_for_DOM_item('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
		return

	#tests to be run have to start with test
	def test_can_start_list_and_retrieve_later(self):
		#Harry becomes sentient and decides to write a to-do. He goes to the
		#superlists website in his web browser
		self.browser.get(self.live_server_url)

		#He notices the page title and header has "To-Do dlists in it"
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#He sees an invitation to enter a to-do item right away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		test_items = ['Learn French', 'Seduce French cats']
		for todo in test_items:
			inputbox = self.wait_for_DOM_item('id_new_item')
			inputbox.send_keys(todo)
			inputbox.send_keys(Keys.ENTER)
			time.sleep(0.5)
		
		for i in range(len(test_items)):
			todo = test_items[i]
			self.check_row_in_list_table('%i: %s' % (i+1,todo))


		#There is another text box to add another item. He types,
		# "enroll in an ornithology class"
		self.fail('Finish the test!')

		#He hits enter, and the page lists both items

		#Harry notices an explanation saying that the site has
		#saved his list permanently using a unique url (the page lists
		#this url and its visible in the address bar)

		#Harry goes to that unique url--and the to-do list is still there

		#Harry then sleeps


####### TODO ########
# -Change the model so that items are associated with a unique list
# -Associate each list with a unique url
# -Want URL to make a new list
# -Want URL to add a new list item.