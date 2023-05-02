def f(n):
    s1 = f'{n:b}'
    if n % 2 != 0:
        s2 = '10' + s1[:-1] + '0'
    else:
        s2 = '11' + s1[:-1] + '1'
    return int(s2, 2)


res = []
for i in range(20, 100):
    res.append(f(i))
print(min(res))