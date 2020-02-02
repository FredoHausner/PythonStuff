import unittest
from selenium import webdriver

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def testChallenge(self):
        self.driver.get('https://www.google.com')
        self.assertion("Google", self.driver.title)


if __name__ == '__main__':
    unittest.main()


# class Rectangle:
#     def __init__(self, widthInFeet, heightInFeet, costPerSquareFoot = 0):
#         self.widthInFeet = widthInFeet
#         self.heightInFeet = heightInFeet
#         self.costPerSqaureFoot = costPerSquareFoot
#
#     def logInfo(self):
#         print(self.widthInFeet, self.heightInFeet, self.costPerSqaureFoot)
#
#     def area(self):
#         return self.widthInFeet * self.heightInFeet
#
#     def costOfLand(self):
#         area = self.area()
#         print('Cost of total land is: ', area * self.costPerSqaureFoot)
#
# r = Rectangle(10, 11)
# r.logInfo()
# r.costOfLand()
#
# b = Rectangle(10,11,400)
# b.logInfo()
# b.costOfLand()