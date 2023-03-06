def phi(n: int):
    """
    Calculate Eulers totient function phi(m).
    Eulers so-called totient function phi(m) is defined as the number of positive integers r (1 <= r < m) that are coprime to m.
    For example: m = 10: r = 1,3,7,9; thus phi(m) = 4. Note the special case: phi(1)

    https://brilliant.org/wiki/eulers-totient-function/

    Example:
    ```
    print(phi(10))

    4
    ```
    """

print(phi(10))
print("\tExpected: 4")