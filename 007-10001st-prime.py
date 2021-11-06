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


def get_nth_prime(n: int) -> int:
    # Q: How to get nth element of generator
    # A: https://stackoverflow.com/questions/2300756/get-the-nth-item-of-a-generator-in-python
    return next(itertools.islice(primes(), n-1, None))


def test_six() -> None:
    assert get_nth_prime(6) == 13


def main() -> None:
    print(get_nth_prime(10_001))


if __name__ == '__main__':
    main()
