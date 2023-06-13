def f(s, c, m):
    if s >= 29:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(s + 6, c + 1, m)]
    if s % 2 == 0:
        moves.append(f(s + 4, c + 1, m))
    else:
        moves.append(f(s + s % 10, c + 1, m))
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 26 + 1):
    for m in range(1, 4 + 1):
        if f(s, 0, m):
            print(s, m)
            break