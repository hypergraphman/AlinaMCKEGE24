for x in '0123456789ABCDE':
    a = int(f'97968{x}21', 15)
    b = int(f'7{x}23', 15)
    n = a + b
    if n % 14 == 0:
        print(n // 14)