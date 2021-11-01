"""
Highly divisible triangular numbers
Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""


def count_divisors(n):
    nDivisors = 1
    i = 2
    while i * i <= n:
        multiplicity = 0
        while n % i == 0:
            n //= i
            multiplicity += 1
        nDivisors *= multiplicity + 1
        i += 1
    if n > 1:
        nDivisors *= 2
    return nDivisors


def solution():
    """Returns the value of the first triangle number to have over five hundred
    divisors.

    >>> solution()
    76576500
    """
    tNum = 1
    i = 1

    while True:
        i += 1
        tNum += i

        if count_divisors(tNum) > 500:
            break

    return tNum


if __name__ == "__main__":
    print(solution())
