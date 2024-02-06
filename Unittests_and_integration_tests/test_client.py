#!/usr/bin/env python3
""" unittests for client.py """
import unittest
from unittest.mock import patch, Mock, PropertyMock
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

    def test_public_repos_url(self):
        """ tests _public_repos_url property from GithubOrgClient """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock,
                   return_value={"repos_url":
                                 "https://api.github.com/orgs/"}) as mock_prop:
            test_instance = GithubOrgClient("repos_url")
            result = test_instance._public_repos_url
            self.assertEqual(result, mock_prop.return_value["repos_url"])
