#! /usr/bin/env python3


def largest_prime_factor(n: int) -> int:
    """
    Gets largest prime factor of :param n:
    """

    largest = 1
    for d in range(2, n+1):
        if n % d == 0:
            largest = max(largest, d)

        while n % d == 0:
            n //= d

        if d * d > n:
            # n doesnt have at two non-trivial divisors here
            break

    # n may be 1 or prime by this point
    largest = max(largest, n)
    return largest


def test_small() -> None:
    assert largest_prime_factor(13_195) == 29


def main() -> None:
    print(largest_prime_factor(600_851_475_143))


if __name__ == '__main__':
    main()
