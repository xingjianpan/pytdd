from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.keys import Keys
import unittest


myProxy = ""

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '' # set this value as desired
    })

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(proxy=proxy)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She
        # goes to check out its homepage
        self.browser.get('http://localhost:8000')


        # She notices the page title adn header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )


# She types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

# when she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do lists


        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
                '1: Buy peacock feathers', [row.text for row in rows],
            "New to-do item did not appear in table --its text was:\n%s" % (
                table.text,
            )
        )

        self.fail('Finish the test')
# There is still a text box inviting her to add another item. She
# enters "Use peakcock feathers to make a fly"
# (Edith is very methodical)

# The page updates again, andnow shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatorytext to that effect.


# she visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')



