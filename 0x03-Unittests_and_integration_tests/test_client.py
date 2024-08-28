#!/usr/bin/env python3
"""
Unit tests for access_nested_map and get_json functions.
"""

from parameterized import parameterized
# from typing import Mapping, Sequence, Any
from unittest.mock import patch, PropertyMock
import unittest
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""
    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, org_n: str, mocked_get_json):
        """Test the org method by mocking the get_json function."""
        mocked_get_json.return_value = {'msg': "payload"}
        instance = GithubOrgClient(org_n)
        instance.org
        mocked_get_json.assert_called_once()

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected one based
        on the mocked payload."""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "addy@glade.com"
            result = GithubOrgClient("Google")._public_repos_url
            self.assertEqual(result, "addy@glade.com")
