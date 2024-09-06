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
                          return_value="https://api.github.com/"
                          ) as pub:
            client = GithubOrgClient("Test value")
            result = client.public_repos()

            self.assertEqual(result, ["Test value"])
            mock_get_json.assert_called_once()
            pub.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, repo, license_key, exp_result):
        """Method to test GithubOrgClient.has_license function"""

        client = GithubOrgClient("Test value")
        result = client.has_license(repo, license_key)
        self.assertEqual(exp_result, result)


if __name__ == '__main__':
    unittest.main()
