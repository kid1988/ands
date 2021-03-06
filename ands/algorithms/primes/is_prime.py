#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Nelson Brochado

Primality Tests.
"""


def is_prime(n):
    """Return `True` if `n` is prime, `False` otherwise."""
    if n < 2:  # primes are greater than 1
        return False
    if n % 2 == 0:
        return n == 2  # returns True if n == 2 because 2 is a prime
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def _is_prime_r(n, i):
    if i * i <= n:
        if n % i == 0:
            return False
        else:
            return _is_prime_r(n, i + 2)
    return True


def is_prime_r(n):
    """Return `True` if `n` is prime, `False` otherwise.

    This function uses recursion.
    In general, you should prefer an iterative approach,
    because the stack has a limit,
    and if exceeded an exception is thrown."""
    if n <= 1:  # primes are greater than 1
        return False
    if n % 2 == 0:
        return n == 2
    return _is_prime_r(n, 3)


def is_prime_2(n):
    """Return `True` if `n` is prime, `False` otherwise.

    This algorithm seems to perform better than `is_prime`.

    **Time Complexity:** O(&radic;<span style="text-decoration:overline;">n</span>/2 * O(n % i == 0))."""
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# TESTS

def test1():
    from time import time
    a = time()
    for i in range(10000000):
        is_prime_2(i)
    # assert is_prime(i) == is_prime_2(i)
    b = time()
    print(b - a)


def test2():
    from time import time
    a = time()
    is_prime_2(10093100991010310111)
    b = time()
    print(b - a)


if __name__ == "__main__":
    test2()
    # test1()
