import cmath
import math


def naive(n: int, x: float) -> complex:
    k = x ** 2
    w = w_k = cmath.rect(1, 4 * math.pi / n)  # w_n ^ 2
    final = 1
    for i in range(1, n >> 1):
        final *= (k - w)
        w *= w_k
    return final


def p_n(n: int, x: float) -> float:
    k = x ** 2
    x_k = 1
    final = 0
    for i in range((n >> 1)):  # n + 1 arithmetic operations
        final += x_k
        x_k *= k
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
