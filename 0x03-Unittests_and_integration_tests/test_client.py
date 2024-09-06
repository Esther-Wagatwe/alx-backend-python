#!/usr/bin/env python3
"""Module to test the client module"""
import unittest
from typing import Dict
from client import GithubOrgClient
from unittest.mock import patch, MagicMock
from utils import get_json
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""
    @parameterized.expand([
        ("google", {"org": "google", "data": "example_data_google"}),
        ("abc", {"org": "abc", "data": "example_data_abc"}),
    ])
    @patch('client.get_json',)
    def test_org(self, org_name, expected_data, mock_json):
        """Test that GithubOrgClient.org returns the expected value."""
        mock_json.return_value = MagicMock(return_value=expected_data)

        client = GithubOrgClient(org_name)

        result = client.org()

        mock_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

        self.assertEqual(result, expected_data)


if __name__ == '__main__':
    unittest.main()
