#!/usr/bin/env python3
"""input mixed list and return float"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers and floats as a float.

    Args:
        mxd_lst (List[Union[int, float]]):
        The list containing integers and/or floats.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return sum(mxd_lst)
