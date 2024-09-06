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
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """Method to test if GithubOrgClient.org returns the correct value"""

        client = GithubOrgClient(org_name)
        res = client.org

        self.assertEqual(res, mock.return_value)
        mock.assert_called_onc


if __name__ == '__main__':
    unittest.main()
