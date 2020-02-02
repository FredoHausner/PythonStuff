from fib import *
from fibString import *
import unittest

class Challenge3(unittest.TestCase):

    fibToFib = 21

    # def setUp(self):
        # self.fibCopy = Fibonacci()
        # self.fibAnswer = self.fibCopy.fib(self.fibToFib)
        # self.fibToString = NumberToString()
        # self.fibAnswerString = self.fibToString.numToString(self.fibAnswer)

    # def tearDown(self):
        # print('Driver Tear Down')

    def testing(self):
        self.fibToString = NumberToString()
        print(self.fibToString.numToString(10567))
        # print(self.fibAnswer, ' - ', self.fibAnswerString)

        # print(self.fibToString.numToString(898))


if __name__ == '__main__':
    unittest.main()