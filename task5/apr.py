def alf(n):
    s1 = f'{n:b}'
    if n % 2 == 0:
        return int('10' + s1, 2)
    else:
        return int('1' + s1 + '01', 2)


res = []
for i in range(9):
    res.append(alf(i))
print(max(res))