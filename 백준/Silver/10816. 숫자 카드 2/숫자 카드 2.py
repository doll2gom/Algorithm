import sys 
from collections import Counter
n = sys.stdin.readline()
lst = list(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
lst2 = list(map(int, sys.stdin.readline().split()))

cnt = Counter(lst)

for l in lst2:
    if l in cnt:
        print(cnt[l], end=' ')
    else:
        print(0, end=' ')