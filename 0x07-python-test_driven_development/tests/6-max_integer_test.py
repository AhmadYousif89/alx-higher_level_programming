#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines the unittest methods for the max_integer function"""

    def test_empty_list(self):
        """Test with empty list."""
        result = max_integer([])
        self.assertEqual(result, None)

    def test_ordered_list(self):
        """Test with an ordered list of integers."""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        result = max_integer([3, 2, 4, 1])
        self.assertEqual(result, 4)

    def test_single_element_list(self):
        """Test with a single element in the list."""
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_floats(self):
        """Test a list of floats."""
        result = max_integer([1.53, 60.3, -19.123, 35.2, 6.0])
        self.assertEqual(result, 60.3)

    def test_mixed_types(self):
        """Test a list of floats."""
        result = max_integer([1, 60.3, -19, 35.2, 6, 90])
        self.assertEqual(result, 90)

    def test_string(self):
        """Test with a string."""
        result = max_integer("Hello")
        self.assertEqual(result, 'o')

    def test_list_of_strings(self):
        """Test with a list of strings."""
        result = max_integer(["max", "string", "is", "this"])
        self.assertEqual(result, "this")

    def test_empty_string(self):
        """Test with an empty string."""
        result = max_integer("")
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
