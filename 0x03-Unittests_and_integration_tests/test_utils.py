#!/usr/bin/env python3
"""
Unit test for access_nested_map function.
"""

from parameterized import parameterized
from typing import Mapping, Sequence, Any
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, n_map: Mapping, path: Sequence, exp: Any):
        """Test access_nested_map with various inputs."""
        self.assertEqual(access_nested_map(n_map, path), exp)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, n_map: Mapping, path: Sequence):
        """"""
        with self.assertRaises(KeyError):
            access_nested_map(n_map, path)
