import sys
N = 1000 - int(sys.stdin.readline())
lst = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in lst:
    cnt += N//i
    N %= i
print(cnt)