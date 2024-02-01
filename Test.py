#!/usr/bin/python3
#testcase for adding 2 no
import unittest
from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two no
        """
        data=[23,32]
        result=summation(data)
        self.assertEqual(result,55)

if __name__ =='__main__':
    unittest.main()
