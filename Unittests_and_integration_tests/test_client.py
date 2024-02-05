#!/usr/bin/env python3
""" unittests for client.py """
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class TestGithubOrgClient(unittest.TestCase):
    """ unittest for GithubOrgClient from client.py """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org, mock_get_json):
        """ tests org method from GithubOrgClient """
        test_instance = GithubOrgClient(test_org)
        test_instance.org
        mock_get_json.assert_called_once()
