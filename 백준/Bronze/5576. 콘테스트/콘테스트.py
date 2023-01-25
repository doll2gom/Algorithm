w = []
k = []
cnt = 0
cnt2 = 0
for i in range(0,10):
    W = int(input())
    w.append(W)
for i in range(0,10):
    K = int(input())
    k.append(K)
for l in range(0,3):
    mw = max(w)
    mk = max(k)
    cnt += mw
    cnt2 += mk
    w.remove(mw)
    k.remove(mk)
print(cnt, cnt2)