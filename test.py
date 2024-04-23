import unittest
from add import addi


class MyTestCase(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(addi(1,2),3)


    def test_add_negative(self):
        self.assertEqual(addi(-1,-1),-2)





if __name__ == '__main__':
    unittest.main()
