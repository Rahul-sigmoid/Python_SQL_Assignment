import unittest
from question4 import Department

class Test_1(unittest.TestCase):

    def test(self):
        # making an object of employee class
        department= Department()
        # calling emp function
        bool=department.dept()
        self.assertEqual(bool,True)


if __name__ == '__main__':
    conn = None
    cur = None
    unittest.main()