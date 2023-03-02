from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n - 1)
    if n > 1 and n % 2 != 0:
        return 2 * f(n - 2)


for i in range(1, 2600, 1):
    f(i)
print(f(2600) - f(2599))