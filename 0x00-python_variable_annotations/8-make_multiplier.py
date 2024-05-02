#!/usr/bin/env python3
"""returns function multip"""


from typing import Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.

    Args:
        multiplier (float): The constant factor to multiply by.

    Returns:
        Callable[[float], float]: A function that
                                  multiplies a float by the multiplier.
    """
    return lambda x: x * multiplier
