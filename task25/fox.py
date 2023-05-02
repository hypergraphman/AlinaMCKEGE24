from fnmatch import fnmatch

for i in range(51, 10**8, 51):
    if fnmatch(str(i), '10*04?23'):
        print(i, i // 51)