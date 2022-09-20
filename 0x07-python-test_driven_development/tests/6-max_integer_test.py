#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer"""
    def test_moduleDocstring(self):
        """check module docstring"""
        module = __import__('6-max_integer').__doc__
        self.assertTrue(len(module) > 1)

    def test_functionDoxstring(self):
        """Checking functions docstring"""
        fxn = max_integer.__doc__
        self.assertTrue(len(fxn) > 1)

    def test_negatives(self):
        """Checking when all list members are negative integers"""
        test_negs = [-1, -9, -5, -4]
        self.assertEqual(max_integer(test_negs), -1)

    def test_all_equal(self):
        """Checking when all list items are the equal"""
        test_eq = [7, 7, 7, 7]
        self.assertEqual(max_integer(test_eq), 7)

    def test_a_negative(self):
        """Checking when one of the list items is a negative"""
        test_neg = [50, 45, -50, 20]
        self.assertEqual(max_integer(test_neg), 50)

    def test_no_arguments(self):
        """Checking when no arguments are passed"""
        self.assertIsNone(max_integer())

    def test_an_emptylist(self):
        """Checking when an empty list is passed"""
        test = []
        self.assertIsNone(max_integer(test))

    def test_maximum_beginning(self):
        """Checking maximum value at the beginning of the list"""
        test_start = [89, 56, 25, 36]
        self.assertEqual(max_integer(test_start), 89)

    def test_maximum_middle(self):
        """Checking maximum value located in the middle of the list"""
        test_middle = [56, 25, 36, 89, 12, 2]
        self.assertEqual(max_integer(test_max), 89)

    def test_maximum_end(self):
        """Checking maximum value at the end of the list"""
        test_end = [36, 25, 56, 89]
        self.assertEqual(max_integer(test_end), 89)

    def test_one_arg(self):
        """Checking a list with only one element"""
        test_solo = [59]
        self.assertEqual(max_integer(test_solo), 59)

    def test_several_max(self):
        """Checking instance of more than one maximum value"""
        test_several = [56, 89, 26, 89, 45]
        self.assertEqual(max_integer(test_several), 89)

    def test_None(self):
        """Check passing None as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_none_int(self):
        """Checking when a none integer argument is passed"""
        test = [58, 25, "String", 36, 7]
        with self.assertRaises(TypeError):
            max_integer(test)


if __name__ == "__main__":
    unittest.main()
