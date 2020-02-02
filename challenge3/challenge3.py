import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')

    def tearDown(self):
        self.driver.close()

    def testing(self):
        self.driver.get('https://www.copart.com')
        WebDriverWait(self.driver, 10).until(
            cond.visibility_of_element_located((By.XPATH, '//*[@id="tabTrending"]/div[1]/div[2]'))
        )
        popularItemsList = self.driver.find_elements_by_xpath('//*[@id="tabTrending"]/div[1]/div[2]//a')

        for item in popularItemsList:
            print(item.get_attribute('text'), '-' ,item.get_attribute('href'))


if __name__ == '__main__':
    unittest.main()