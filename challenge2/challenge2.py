# For this challenge, look through the different ways to do assertions.  Then write a script that will go to copart.com, search for exotics and verify porsche is in the list of cars.  Use the hard assertion for this challenge.

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond


# vvv assertEqual vvv
# self.assertEqual(value, 'should be equal to this value', 'this is the message that is printed if not equal')

# vvv get attributes in python, possible attributes would be 'value', 'innerHTML', 'class', etc...
# element = self.driver.find_element_by_css_selector('q')
# element_inner_HTML = element.get_attribute('innerHTML')


class Challenge2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')

    def tearDown(self):
        self.driver.close()

    def testing(self):
        self.driver.get('https://www.copart.com')
        searchInput = WebDriverWait(self.driver, 10).until(
            cond.visibility_of_element_located((By.CSS_SELECTOR, '#input-search'))
        )
        searchInput.send_keys('exotic')
        searchInput.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(
            cond.visibility_of_element_located((By.XPATH, "//table[@id='serverSideDataTable']/tbody/tr[1]/td[5]")))
        assert 'PORSCHE' in self.driver.page_source



if __name__ == '__main__':
    unittest.main()
