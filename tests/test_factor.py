import unittest

import sys, os

sys.path.insert(0, os.path.pardir)

from test_base_class import ListTestCase

import factorization

class FactorTestCase(ListTestCase):
    def test_non_int(self):
        self.assertSequenceEqual([], factorization.factor(0.1))

    def test_to_ten(self):
        self.assertSequenceEqual([0], factorization.factor(0))

        self.assertSequenceEqual([1], factorization.factor(1))

        self.assertSequenceEqual([2], factorization.factor(2))

        self.assertSequenceEqual([3], factorization.factor(3))

        self.assertSequenceEqual([2, 2], factorization.factor(4))

        self.assertSequenceEqual([5], factorization.factor(5))

        self.assertSequenceEqual([2, 3], factorization.factor(6))

        self.assertSequenceEqual([7], factorization.factor(7))

        self.assertSequenceEqual([2, 2, 2], factorization.factor(8))

        self.assertSequenceEqual([3, 3], factorization.factor(9))

        self.assertSequenceEqual([2, 5], factorization.factor(10))

    def test_ten_to_twenty(self):
        self.assertSequenceEqual([11], factorization.factor(11))

        self.assertSequenceEqual([2, 2, 3], factorization.factor(12))

        self.assertSequenceEqual([13], factorization.factor(13))

        self.assertSequenceEqual([2, 7], factorization.factor(14))

        self.assertSequenceEqual([3, 5], factorization.factor(15))

        self.assertSequenceEqual([2, 2, 2, 2], factorization.factor(16))

        self.assertSequenceEqual([17], factorization.factor(17))

        self.assertSequenceEqual([2, 3, 3], factorization.factor(18))

        self.assertSequenceEqual([19], factorization.factor(19))

        self.assertSequenceEqual([2, 2, 5], factorization.factor(20))

    def test_ten_to_one_hundred(self):
        self.assertSequenceEqual([23], factorization.factor(23))
        self.assertSequenceEqual([2, 2, 3, 3], factorization.factor(36))
        self.assertSequenceEqual([2, 3, 7], factorization.factor(42))
        self.assertSequenceEqual([3, 5, 5], factorization.factor(75))


if __name__ == '__main__':
    unittest.main()
