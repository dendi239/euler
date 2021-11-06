#! /usr/bin/env python3

import typing as tp


def is_pythagorean_triplet(a: int, b: int, c: int) -> int:
    return a ** 2 + b ** 2 == c ** 2


def find_triple(s: int) -> tp.Tuple[int, int, int]:
    for a in range(1, s):
        for b in range(1, s-a):
            if is_pythagorean_triplet(a, b, s - a - b):
                return (a, b, s - a - b)


def test_small() -> None:
    assert find_triple(12) == (3, 4, 5)


def main() -> None:
    a, b, c = find_triple(1_000)
    print(a * b * c)


if __name__ == '__main__':
    main()
