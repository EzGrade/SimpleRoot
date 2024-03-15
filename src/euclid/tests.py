import unittest

from .main import gcd


class TestGCD(unittest.TestCase):

    def test_1(self):
        self.assertEqual(gcd(10, 25), 5)

    def test_2(self):
        self.assertEqual(gcd(14, 15), 1)

    def test_3(self):
        self.assertEqual(gcd(3, 9), 3)
