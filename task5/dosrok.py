def f(n):
    s1 = f'{n:b}'
    if n % 3 == 0:
        s2 = s1[-3:] + s1
    else:
        s2 = f'{(n % 3) * 3:b}' + s1
    return int(s2, 2)


print(f(6))
print(f(4))

for barbariska in range(100):
    if f(barbariska) > 125:
        print(barbariska)
        break