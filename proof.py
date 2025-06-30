import cmath
import math


def naive(n: int, x: float) -> complex:
    k = x ** 2
    w_k = cmath.rect(1, 4 * math.pi / n)  # w_n ^ 2
    final = 1
    w = 1
    for i in range((n >> 1) - 1):
        w *= w_k
        final *= (k - w)
    return final


def p_n(n: int, x: float) -> float:
    k = x ** 2  # 1 operation
    """
    x_k = 1
    final = 1
    for i in range((n >> 1) - 1):  # n - 2 arithmetic operations
        x_k *= k
        final += x_k
    """
    final = 1 + k  # 1 operation
    for i in range((n >> 1) - 2):  # n - 4 operations
        final = 1 + k * final
    return final


def p_n_1(n: int) -> int:
    return n >> 1  # O(1) since bit shifts are constant time operations


def sdft(n: int) -> list:
    y = [0] * n
    k = n >> 1  # one bit shift
    y[0] = k  # two assignments
    y[k] = k  # overall time is O(1) since bit shifts are constant time operations
    return y


def scoeff(n: int) -> list:
    y = [0] * n
    y[0::2] = [1] * (n >> 1)  # this should be O(n) since there are n/2 assignments. I do not know how that works.
    return y  # or O(1) since only arithmetic operations are counted.


print(naive(10, 6))
print(p_n(10, 6))
print(p_n_1(10))
print(sdft(10))
print(scoeff(10))
