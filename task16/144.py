from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 2 == 0:
        return 1 + f(n // 2)
    if n < 10000 and n % 2 != 0:
        return n ** 2 + f(n + 2)


for i in range(10000, 1, -1):
    try:
        f(i)
    except:
        pass

print(f(192) - f(9))

