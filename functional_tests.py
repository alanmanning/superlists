from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.PhantomJS()

	def tearDown(self):
		self.browser.quit()

	#tests to be run have to start with test
	def test_can_start_list_and_retrieve_later(self):
		#Harry becomes sentient and decides to write a to-do. He goes to the
		#superlists website in his web browser
		self.browser.get('http://localhost:8000')

		#He notices the page title has "To-Do dlists in it"
		self.assertIn('To-Do', self.browser.title)

		self.fail('Finish the test!')

		#He also notices the word "To-Do" in the page header

		#He sees an invitation to enter a to-do item right away

		#He types "learn French" into the text box

		#When he hits enter, the page updates, and the page lists:
		# "1: learn French"

		#There is another text box to add another item. He types,
		# "enroll in an ornithology class"

		#He hits enter, and the page lists both items

		#Harry notices an explanation saying that the site has
		#saved his list permanently using a unique url (the page lists
		#this url and its visible in the address bar)

		#Harry goes to that unique url--and the to-do list is still there

		#Harry then sleeps


if __name__ == '__main__':
	unittest.main()