s = set()
for i in range(500, 5000 + 1):
    st1 = f'{i:b}'
    st2 = st1[1:]
    # t = st2.lstrip('0')
    st3 = int(st2, 2)
    r = i - st3
    s.add(r)
print(s)
print(len(s))
