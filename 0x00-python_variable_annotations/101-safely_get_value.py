#!/usr/bin/env python3
'''Task 11's module.
'''


from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Returns the value associated with the key in the dictionary,
    or a default value if the key is not present.

    Args:
        dct (Dict[K, V]): The input dictionary.
        key (K): The key to search for in the dictionary.
        default (Optional[V], optional): The default value to return if
                                         the key is not found. Defaults
                                         to None.

    Returns:
        V: The value associated with the key in the dictionary,
           or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
