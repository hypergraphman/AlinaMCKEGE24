from itertools import permutations

s = set()
for word in permutations('КАПКАН', r=6):
    word = ''.join(word)
    if word.count('КК') != 1 and word.count('АА') != 1:
        s.add(word)
print(len(s))
