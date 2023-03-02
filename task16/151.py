from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 10:
        return n
    if n >= 10000:
        return 1
    if 10 < n < 10000 and n % 2 == 0:
        return n % 10 + f(n + 2)
    if 10 < n < 10000 and n % 2 != 0:
        return f(n - 2) - (n - 1) % 10


for i in range(1, 10000, 1):
    f(i)

for i in range(10000, 1, -2):
    f(i)

print(f(4500) + f(5515))

