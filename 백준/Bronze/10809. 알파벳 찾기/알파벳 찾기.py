S = str(input())
s = []
for n in range(97,123):
    if chr(n) in S:
        s.append(S.find(chr(n)))
    else:
        s.append(-1)
print(*s)