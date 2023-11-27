import unittest
import sys

"""
Contain a single class:
TestMaxInteger - it is a test class
that is used to test if max_integer function
works as expected. which returns the largest
element in a list
>>> max_integer([1, 2, 3, 4])
4
"""

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    It is used to test if max_integer function works
    as expected. which returns the largest element in a list
    >>> max_integer([40, 60, 30, -503])
    60
    """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([60, -5, 200, -43, -433]), 200)
        self.assertEqual(max_integer([2.3, 0.3, 0.03, 4.4]), 4.4)
        self.assertRaises(TypeError, max_integer, 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-0.33, 60, -4.53, 1, 0]), 60)
        self.assertEqual(max_integer("string"), 't')
        self.assertEqual(max_integer("t"), 't')
        self.assertRaises(TypeError, max_integer, [1, '3', 4, '5'])
        self.assertRaises(TypeError, max_integer, [1, '544', 5])
