#!/usr/bin/env python3
"""
Module to test the client module
"""
import unittest
from typing import Dict
from client import GithubOrgClient
from unittest.mock import patch, MagicMock, PropertyMock
from utils import get_json
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json',)
    def test_org(self, org_name, expected_data, mock_json):
        """
        Test that GithubOrgClient.org returns the expected value.
        """
        mock_json.return_value = MagicMock(return_value=expected_data)

        client = GithubOrgClient(org_name)

        result = client.org()

        mock_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
            )

        self.assertEqual(result, expected_data)

    def test_public_repos_url(self):
        """
        Test GithubOrgClient._public_repos_url returns the correct URL.
        """
        mocked_org_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
            }

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mocked_org_payload

            client = GithubOrgClient("google")

            self.assertEqual(client._public_repos_url,
                             mocked_org_payload["repos_url"]
                             )
            mock_org.assert_called_once()

@patch("client.get_json", return_value=[{"name": "Test value"}])
def test_public_repos(self, mock_get_json):
    """
    Test GithubOrgClient.public_repos returns the expected list of repos.
    """
    with patch.object(GithubOrgClient, '_public_repos_url',
                      new_callable=PropertyMock,
                      return_value="https://api.github.com/") as mock_public_url:
        # Create a GithubOrgClient instance
        client = GithubOrgClient("TestOrg")
        
        # Call the method being tested
        repos = client.public_repos()
        
        # Check if the public_repos method returns the expected result
        self.assertEqual(repos, ["Test value"])
        
        # Ensure get_json was called once with the correct URL
        mock_get_json.assert_called_once_with("https://api.github.com/")
        
        # Ensure _public_repos_url property was accessed once
        mock_public_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()
