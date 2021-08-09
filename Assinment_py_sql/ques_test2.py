import unittest
from question2 import Compensation

class Test_1(unittest.TestCase):

    def test(self):
        # making an object of employee class
        compensation = Compensation()
        # calling emp function
        bool=compensation.com()
        self.assertEqual(bool,True)


if __name__ == '__main__':
    conn = None
    cur = None
    unittest.main()