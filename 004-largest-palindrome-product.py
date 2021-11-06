#! /usr/bin/env python3


def is_palindrome(n: int) -> int:
    return str(n) == str(n)[::-1]  # compare string representation of n to itself, but reversed


def largest_palindrome_product(digits: int) -> int:
    return max(x * y
               for x in range(10 ** (digits - 1), 10 ** digits)  # iterate over all pairs
               for y in range(10 ** (digits - 1), 10 ** digits)  # of ${digits}-digits numbers
               if is_palindrome(x * y))  # check result to be palindrome


def test_small() -> None:
    assert largest_palindrome_product(2) == 9009


def main() -> None:
    print(largest_palindrome_product(3))


if __name__ == '__main__':
    main()
