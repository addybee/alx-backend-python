#!/usr/bin/env python3
"""
    this modile contains function that Safely retrieves a value from
    a dictionary based on the given key.
"""
from typing import Any, Mapping, Optional, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary based on the given key.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to search for in the dictionary.
        default (Optional[T], optional): The default value to return
        if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
