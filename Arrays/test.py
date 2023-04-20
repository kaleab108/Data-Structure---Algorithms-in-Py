import sys
sys.setrecursionlimit(10000)


def factorial(n):
    assert n >= 0 and int(n) == n, "the number must be postive integer only!"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(15))
