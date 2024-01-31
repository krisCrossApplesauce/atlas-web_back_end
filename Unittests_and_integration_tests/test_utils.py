#!/usr/bin/env python3
""" unittest for utils.py """
access_nested_map = __import__('utils').access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ unittest for access_nested_map from utils.py """

    @parameterized.expand([
        (),
    ])
    def test_access_nested_map(self):
        """ tests access_nested_map """
        pass
