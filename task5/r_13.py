n = 1
r = 6
while r <= 77:
    n = n + 1
    step1 = f'{n:b}'
    step2 = step1 + str(sum(map(int, step1)) % 2)
    step3 = step2 + str(sum(map(int, step2)) % 2)
    r = int(step3, 2)
print(n)
