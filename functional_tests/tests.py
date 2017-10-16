from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import pdb


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	#tests to be run have to start with test
	def test_can_start_list_and_retrieve_later(self):
		#Harry becomes sentient and decides to write a to-do. He goes to the
		#superlists website in his web browser
		self.browser.get('http://localhost:8000')

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
			inputbox = self.browser.find_element_by_id('id_new_item')
			inputbox.send_keys(todo)
			inputbox.send_keys(Keys.ENTER)
			time.sleep(2)
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertEqual(len(test_items),len(rows),
			'For rows only got: ' + str([row.text for row in rows]))

		#There is another text box to add another item. He types,
		# "enroll in an ornithology class"
		self.fail('Finish the test!')

		#He hits enter, and the page lists both items

		#Harry notices an explanation saying that the site has
		#saved his list permanently using a unique url (the page lists
		#this url and its visible in the address bar)

		#Harry goes to that unique url--and the to-do list is still there

		#Harry then sleeps


if __name__ == '__main__':
	unittest.main()