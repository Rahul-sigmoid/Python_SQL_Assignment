import unittest
from question1 import Employees

class Test_1(unittest.TestCase):

    def test(self):
        # making an object of employee class
        employee = Employees()
        # calling emp function
        bool=employee.emp()
        self.assertEqual(bool,True)


if __name__ == '__main__':
    conn = None
    cur = None
    unittest.main()