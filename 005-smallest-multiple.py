#! /usr/bin/env python3

import functools


def gcd(a: int, b: int) -> int:
    """Greatest common divisor of :param a: and :param b:"""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Least common multiplier of :param a: and :param b:"""
    return a // gcd(a, b) * b


def smallest_multiple(n: int) -> int:
    return functools.reduce(lcm, range(1, n+1))


def test_small() -> None:
    assert smallest_multiple(10) == 2520


def main() -> None:
    print(smallest_multiple(20))


if __name__ == '__main__':
    main()
