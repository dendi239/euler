#! /usr/bin/env python3

import itertools
import typing as tp


def fibbonaccies() -> tp.Generator[int, None, None]:
    """
    Generator for fibbonacci numbers

    This is generator for fibbonacci numbers, works in linear way by
     keeping state of two concecutive values.

    fibs = fibbonaccies()
    assert 0 == next(fibs)
    assert 1 == next(fibs)
    assert 1 == next(fibs)
    """
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0 + f1


def test_fibs() -> None:
    fibs = fibbonaccies()

    assert 0 == next(fibs)
    assert 1 == next(fibs)
    assert 1 == next(fibs)
    assert 2 == next(fibs)


def sum_small_even_fibs(n: int) -> int:
    return sum(x for x in itertools.takewhile(lambda x: x < n, fibbonaccies()) if x % 2 == 0)


def test_small_sum() -> None:
    assert sum_small_even_fibs(15) == 2 + 8
    assert sum_small_even_fibs(100) == 2 + 8 + 34


def main() -> None:
    print(sum_small_even_fibs(4_000_000))


if __name__ == '__main__':
    main()
