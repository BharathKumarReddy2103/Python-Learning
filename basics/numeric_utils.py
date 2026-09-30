"""This module contains the utility functions which operate on numbers
"""


def is_even(number: int) -> bool:
    """Check whether the number is even or not.

    Args:
        number (int): number to  be passed

    Returns:
        bool: True if even, False otherwise.
    """
    return number % 2 == 0

def is_prime(number: int) -> bool:
    """Check whether the number is prime or not.

    Args:
        number (int): number to  be passed

    Returns:
        bool: True if prime, False otherwise.
    """
    if number < 2:
        return False
    index = 2
    while index < number:
        if number % index == 0:
            return False
        index += 1
    return True


def sum_of_multiples_of_3_or_5(start: int=1, end: int=10) -> int:
    """Calculate the sum of multiples of 3 or 5 between start and end.

    Args:
        start (int, optional): starts. Defaults to 1.
        end (int, optional): end. Defaults to 10.

    Returns:
        int: The sum of multiples of 3 or 5 between start and end.
    """
    result = 0
    while start <= end:
        if start % 3 == 0 or start % 5 == 0:
            result += start
        start += 1
    return result