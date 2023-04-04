*a, = map(int, open('17-282.txt').read().split())
mn17 = 10**10
for el in a:
    if el < mn17 and el % 17 == 0:
        mn17 = el
res = []
for p1, p2 in zip(a, a[1:]):
    if p1 % mn17 == 0 or p2 % mn17 == 0:
        res.append(p1 + p2)
print(len(res), max(res))