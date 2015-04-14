import unittest

import sys, os, math

sys.path.insert(0, os.path.pardir)

from test_base_class import ListTestCase

import factorization

class PrimesTestCase(ListTestCase):
    def test_first_one_hundred(self):
        self.assertSequenceEqual(
            [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541],
            factorization.primes(542))

    def test_cutoff(self):
        self.assertSequenceEqual([2, 3, 5, 7], factorization.primes(7))

    def test_ask_for_less(self):
        self.assertSequenceEqual([2, 3, 5, 7, 11, 13, 17, 19], factorization.primes(20))
        self.assertSequenceEqual([2, 3, 5, 7], factorization.primes(10))
        self.assertSequenceEqual([2], factorization.primes(2))

    def test_pass_in_more(self):
        self.assertSequenceEqual([2, 3, 5, 7], factorization.primes(10, factorization.primes(20)))


if __name__ == '__main__':
    unittest.main()
