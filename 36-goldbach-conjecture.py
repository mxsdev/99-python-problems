def goldbach_pair(n: int):
    """
    Goldbachs conjecture says that every positive even number greater than 2 is the sum of two prime numbers. Example: 28 = 5 + 23. It is one of the most famous facts in number theory that has not been proved to be correct in the general case. It has been numerically confirmed up to very large numbers.

    Write a predicate to find the two prime numbers that sum up to a given even number.

    Example:
    ```
    print(goldbach_pair(28))
    print(goldbach_pair(1856))

    (5, 23)
    (67, 1789)
    ```
    """

print(goldbach_pair(28))
print("\tExpected: (5, 23)")

print(goldbach_pair(1856))
print("\tExpected: (67, 1789)")
