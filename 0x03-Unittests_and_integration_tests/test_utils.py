#!/usr/bin/env python3
"""Module to test the utils module"""
import unittest
from utils import access_nested_map, get_json, memoize
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


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator."""
    def test_memoize(self):
        """Test that memoize decorator caches results."""
        class TestClass:
            """Class that defines attributes to test memoize"""
            def a_method(self):
                """Method that returns an instance of memoize class"""
                return 42

            @memoize
            def a_property(self):
                """Method that defines a property instance of memoize"""

                return self.a_method()


        test_instance = TestClass()
        with patch.object(test_instance, 'a_method',
                          return_value=42) as mock_a_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(result1, result2)

    if __name__ == "__main__":
        unittest.main()
