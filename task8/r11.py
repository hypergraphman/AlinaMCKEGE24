from itertools import product

count = 0
for word in product('ШКОЛА', repeat=3):
    word = ''.join(word)
    if word.count('К') == 1:
        count += 1
print(count)