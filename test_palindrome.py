import unittest
from test1 import testfunction

class TestPalidromeFunction(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(testfunction.palidrome_function(''))

    def test_simple_palindrome(self):
        self.assertTrue(testfunction.palidrome_function('madam'))
    
    def test_non_palindrome(self):
        self.assertFalse(testfunction.palidrome_function('hello'))


if __name__ == '__main__':
    unittest.main()