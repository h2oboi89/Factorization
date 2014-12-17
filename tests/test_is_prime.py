import unittest

import sys, os

sys.path.insert(0, os.path.pardir)

from test_base_class import ListTestCase

import factorization
        
class IsPrimeTestCase(unittest.TestCase):
    def test_negative(self):
        self.assertFalse(factorization.is_prime(-1))
        self.assertFalse(factorization.is_prime(0))
        
    def test_to_ten(self):
        self.assertFalse(factorization.is_prime(1))
        self.assertTrue(factorization.is_prime(2))
        self.assertTrue(factorization.is_prime(3))
        self.assertFalse(factorization.is_prime(4))
        self.assertTrue(factorization.is_prime(5))
        self.assertFalse(factorization.is_prime(6))
        self.assertTrue(factorization.is_prime(7))
        self.assertFalse(factorization.is_prime(8))
        self.assertFalse(factorization.is_prime(9))
        self.assertFalse(factorization.is_prime(10))
        
if __name__ == '__main__':
    unittest.main()