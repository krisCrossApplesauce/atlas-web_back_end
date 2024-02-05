#!/usr/bin/env python3
""" unittest for utils.py """
access_nested_map = __import__('utils').access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ unittest for access_nested_map from utils.py """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), ({"b": 2}, 2))
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ tests access_nested_map """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
