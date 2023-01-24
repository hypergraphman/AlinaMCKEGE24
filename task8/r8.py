from itertools import permutations

s = set()
for word in permutations('УЛЕЙ'):
    word = ''.join(word)
    if word[0] != 'Й' and 'ЕУ' not in word:
        s.add(word)
print(len(s))
