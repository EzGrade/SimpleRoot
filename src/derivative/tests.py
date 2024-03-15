import unittest

from .main import Derivative


class TestDerivative(unittest.TestCase):
    def setUp(self):
        self.d = Derivative('x^2 + 2x + 1')

    def test_split(self):
        self.assertEqual(self.d.split(), ['x^2', '+', '2x', '+', '1'])
