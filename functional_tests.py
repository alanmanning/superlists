from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


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

		#He types "learn French" into the text box
		inputbox.send_keys('Learn French')

		#When he hits enter, the page updates, and the page lists:
		# "1: learn French"
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Learn French' for row in rows),
			'New to-do item did not appear in table'
		)

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