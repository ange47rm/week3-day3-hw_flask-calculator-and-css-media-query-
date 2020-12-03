import unittest

from calculator import *


class TestCalculator (unittest.TestCase):

    def test_add (self):
        self.assertEqual ("The answer is 4", add(2,2))

    def test_subtract (self):
        self.assertEqual ("The answer is 4", subtract(6,2))

    def test_multiply (self):
        self.assertEqual ("The answer is 16", multiply(8,2))

    def test_divide (self):
        self.assertEqual ("The answer is 9.0", divide(81,9))