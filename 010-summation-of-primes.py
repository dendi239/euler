#! /usr/bin/env python3

import itertools
import typing as tp


def primes() -> tp.Generator[int, None, None]:
    primes_ = []
    d = 2

    while True:
        is_prime = True
        for p in primes_:
            if p * p > d:
                break

            if d % p == 0:
                is_prime = False
                break

        if is_prime:
            primes_.append(d)
            yield d

        d += 1


def sum_primes_below(n: int) -> int:
    return sum(itertools.takewhile(lambda x: x < n, primes()))


def test_ten() -> None:
    assert sum_primes_below(10) == 17


def main() -> None:
    print(sum_primes_below(2_000_000))


if __name__ == '__main__':
    main()
