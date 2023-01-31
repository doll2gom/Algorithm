from itertools import zip_longest

lst =[]
trans_words = []
words = [ list(map(str,input().split())) for _ in range(5)]
for w in words:
    for w2 in zip_longest(range(15),w[0], fillvalue=None):
        if w2[1] != None:
            lst.append(w2)
for n in range(15):
    for l in lst:
        if l[0] ==n:
            trans_words.append(l[1])

print(*trans_words,sep='')