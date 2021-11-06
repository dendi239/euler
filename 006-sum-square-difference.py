#! /usr/bin/env python3


def sum_square_difference(n: int) -> int:
    """
    Calculates following formula:

    (1 + 2 + ... + n)^2 - (1^2 + ... + n^2)
    """
    return sum(range(1, n+1)) ** 2 - sum(x ** 2 for x in range(1, n+1))


def test_ten() -> None:
    assert sum_square_difference(10) == 2640


def main() -> None:
    print(sum_square_difference(100))


if __name__ == '__main__':
    main()
