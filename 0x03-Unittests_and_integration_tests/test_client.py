#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient.
"""

from parameterized import parameterized, parameterized_class
from typing import Dict
from unittest.mock import patch, PropertyMock, Mock
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient."""

    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, org_n: str, mocked_get_json):
        """Test the org property by mocking the get_json function."""
        mocked_get_json.return_value = {'login': org_n}
        instance = GithubOrgClient(org_n)
        self.assertEqual(instance.org, mocked_get_json.return_value)
        mocked_get_json.assert_called_once()

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is as expected
        based on the mocked payload."""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "api.github.com/orgs/Google"
            result = GithubOrgClient("Google")._public_repos_url
            self.assertEqual(result, "api.github.com/orgs/Google")

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """Test the public_repos method."""
        mocked_get_json.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'}
        ]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:

            mock_public_repos_url.return_value = "api.github.com/orgs/Google"

            client = GithubOrgClient("Google")
            repos = client.public_repos()
            self.assertEqual(repos, ['repo1', 'repo2'])
            mocked_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict[str, Dict], license_key: str,
                         expected: bool):
        """Test has_licence method"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up the class-level patch for requests.get."""
        cls.patcher = patch('requests.get', autospec=True)
        get_patcher = cls.patcher.start()

        # Define the side_effect function to return the correct payload
        def get_side_effect(url, *args, **kwargs):
            mock_response = Mock()
            if url != cls.org_payload.get('repos_url'):
                mock_response.json.return_value = cls.org_payload
            else:
                mock_response.json.return_value = cls.repos_payload
            return mock_response

        get_patcher.side_effect = get_side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method."""
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)
        repos = client.public_repos("apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
