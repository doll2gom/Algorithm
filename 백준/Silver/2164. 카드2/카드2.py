import sys
from collections import deque
N = deque( n for n in range(1, int(sys.stdin.readline())+1))
for n in range(len(N)-1):
    N.popleft()
    N.rotate(-1)
    if len(N) == 0:
        break
print(N[0])