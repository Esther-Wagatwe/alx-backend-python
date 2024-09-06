#!/usr/bin/env python
"""Module to test the client module"""
import unittest
from typing import Dict
from client import GithubOrgClient
from unittest.mock import patch, MagicMock
from utils import get_json
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""
    @parameterized.expand(["google", "abc"])
    @patch('client.get_json')
    def test_org(self, org: str, getJson: MagicMock) -> None:
        """
        Tests the org property of GithubOrgClient class
        Args:
            org (str): organization
            getJson (MagicMock): a MagicMock object of `get_json` funtion
        Returns:
            None
        """
        gitClient = GithubOrgClient(org)
        self.assertEqual(gitClient.org, getJson.return_value)
        getJson.assert_called_once_with(gitClient.ORG_URL.format(org=org))


if __name__ == '__main__':
    unittest.main()
