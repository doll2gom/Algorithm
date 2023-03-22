import sys
from collections import deque
N = int(sys.stdin.readline())
for case in range(1, N+1):
    q = deque()
    n = map(str, sys.stdin.readline().split())
    for w in n:
        q.appendleft(w)
    print(f'Case #{case}: {" ".join(q)}')