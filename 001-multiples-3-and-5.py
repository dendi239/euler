#! /usr/bin/env python3


def sum_multiples(n: int) -> int:
    """
    Get sum of multiples 3 and 5 below :param: n.

    Example:
        n = 10 -> 3 + 5 + 6 + 9 = 23
    """
    return sum(x for x in range(n) if x % 5 == 0 or x % 3 == 0)


def test_ten() -> None:
    assert sum_multiples(10) == 23


def main() -> None:
    print(sum_multiples(1000))


if __name__ == '__main__':
    main()
