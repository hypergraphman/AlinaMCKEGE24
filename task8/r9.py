from itertools import permutations

s = set()
for word in permutations('ВУАЛЬ'):
    word = ''.join(word)
    if word[0] != 'Ь' and 'ЬУ' not in word and 'ЬА' not in word:
        s.add(word)
print(len(s))
