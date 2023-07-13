import sys
N = int(sys.stdin.readline())
lst = []
for n in range(N):
    w = sys.stdin.readline().strip()
    if w not in lst:
        lst.append(w)
lst.sort()
lst.sort(key=len)
for a in range(len(lst)):
    print(lst[a])
