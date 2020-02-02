from autobots import SwitchWeek
import unittest



class switch(unittest.TestCase):

    def test(self):
        switch = SwitchWeek()
        print(switch.switch('REAR END'))



if __name__ == '__main__':
    unittest.main()