T = int(input())
for t in range(0,T):
    W = list(map(str,input().split()))
    lst = []
    for w in W:
        rev_w = w[::-1]
        lst.append(rev_w)
    print(*lst)