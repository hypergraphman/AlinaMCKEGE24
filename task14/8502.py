for x in range(0, 14 + 1):
    a = 9 * 15 ** 7 + 9 * 15 ** 6 + 6 * 15 ** 5 + 5 * 15 ** 4 + 8 * 15 ** 3 + x * 15 ** 2 + 2 * 15 + 9
    b = 1 * 15 ** 6 + 2 * 15 ** 4 + x * 15 ** 3 + 2 * 15 + 3
    v = a + b
    if v % 14 == 0:
        print(v // 14, x)