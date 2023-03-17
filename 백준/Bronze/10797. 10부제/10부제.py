import sys
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
cnt = 0
for l in lst:
    if l == n:
        cnt += 1
print(cnt)