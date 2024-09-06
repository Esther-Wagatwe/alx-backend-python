#!/usr/bin/env python3
"""Module to test the utils module"""
import unittest
from utils import access_nested_map, get_json
from unittest.mock import patch
from utils import get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map with different inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for missing keys."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception),
                         f"'{path[len(nested_map):][0]}'")


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns expected JSON data."""
        mock_get.return_value = test_payload
        res = get_json(test_url)
        self.assertEqual(res, test_payload)

    if __name__ == "__main__":
        unittest.main()
