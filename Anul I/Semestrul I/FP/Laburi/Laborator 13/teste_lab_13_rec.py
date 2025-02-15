import unittest
from lab_13_rec import has_common_digit, is_valid_sequence, find_subsequences

class TestSequenceFunctions(unittest.TestCase):

    def test_has_common_digit(self):
        self.assertTrue(has_common_digit(123, 321))  
        self.assertTrue(has_common_digit(456, 654))  
        self.assertFalse(has_common_digit(123, 789))  
        self.assertFalse(has_common_digit(0, 987))    

    def test_is_valid_sequence(self):
        self.assertTrue(is_valid_sequence([12, 23, 34]))  
        self.assertFalse(is_valid_sequence([12, 24, 35]))  
        self.assertFalse(is_valid_sequence([45, 44, 46]))  

    def test_find_subsequences(self):
        self.assertEqual(find_subsequences([11, 12, 22, 33]), [[11, 12, 22]])
        self.assertEqual(find_subsequences([11, 22, 33]), [])  
        self.assertEqual(find_subsequences([1, 12, 23, 34, 45, 56]), [[1, 12, 23],[1, 12, 23, 34],[1, 12, 23, 34, 45],[1, 12, 23, 34, 45, 56],[12, 23, 34],[12, 23, 34, 45],[12, 23, 34, 45, 56],[23, 34, 45],[23, 34, 45, 56],[34, 45, 56]])

if __name__ == "__main__":
    unittest.main()
