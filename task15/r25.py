for a in range(1, 1000):
    if all((x & 125 != 1) or ((x & 34 == 2) <= (x & a == 0)) for x in range(1, 1000)):
        print(a)