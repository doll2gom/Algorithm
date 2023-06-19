lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
words = str(input())

for w in lst:
    words = words.replace(w, '@')
print(len(words))