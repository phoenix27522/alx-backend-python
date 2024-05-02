#!/usr/bin/env python3
"""task 9"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains
    an element from the input list and its length.

    Args:
        lst (List[str]): The input list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples where the
                               first element is a string from the input list
        and the second element is its length.
    """
    return [(i, len(i)) for i in lst]
