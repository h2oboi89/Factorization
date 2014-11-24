import unittest

import sys, os

sys.path.insert(0, os.path.pardir)

from test_base import ListTestCase

import factorization

class PrimesTestCase(ListTestCase):
    def test_to_ten(self):
        self.assertSequenceEqual([2, 3, 5, 7], factorization.primes(10))
        
    def test_cutoff(self):
        self.assertSequenceEqual([2, 3, 5, 7], factorization.primes(7))
        
    def test_to_twenty(self):
        self.assertSequenceEqual([2, 3, 5, 7, 11, 13, 17, 19], factorization.primes(20))
        
    def test_ask_for_less(self):
        self.assertSequenceEqual([2, 3, 5, 7, 11, 13, 17, 19], factorization.primes(20))
        self.assertSequenceEqual([2, 3, 5, 7], factorization.primes(10))
        self.assertSequenceEqual([2], factorization.primes(2))
        
if __name__ == '__main__':
    unittest.main()