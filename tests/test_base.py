import unittest

class ListTestCase(unittest.TestCase):
    def assertSequenceEqual(self, expected, actual):
        self.assertEqual(len(expected), len(actual))
        
        for e, a in zip(expected, actual):
            self.assertEqual(e, a)