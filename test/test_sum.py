import unittest

from sum import sum 

class test_sum(unittest.TestCase):

    def test_list_int(self):
        """ Test that it can sum a list of integers """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result,6, "Incorret sum of integers")

    def test_list_float(self):
        """ Test that it can sum a list of floats """
        data = [1.2, 2.3, 3.4]
        result = sum(data)
        self.assertEqual(result,6.9, "Incorret sum of floats")

    def test_list_negative(self):
        """ Test that it can sum a list of negative numbers """
        data = [-4, -2, -1]
        result = sum(data)
        self.assertEqual(result, -7, "Incorret sum of negative numbers")
    
    
if __name__ == '__main__':
    unittest.main()