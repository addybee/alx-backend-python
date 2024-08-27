#!/usr/bin/env python3
"""
Unit tests for access_nested_map and get_json functions.
"""

from parameterized import parameterized
from typing import Mapping, Sequence, Any
from unittest.mock import patch
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, n_map: Mapping, path: Sequence, expected: Any):
        """Test access_nested_map returns correct output for valid inputs."""
        self.assertEqual(access_nested_map(n_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, n_map: Mapping, path: Sequence):
        """Test access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError):
            access_nested_map(n_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.get_json')
    def test_get_json(self, url: str, expected: dict, mock_get_json):
        """Test get_json returns expected output for given URLs."""
        mock_get_json.return_value = expected
        self.assertEqual(mock_get_json(url), expected)
        mock_get_json.assert_called_once_with(url)
