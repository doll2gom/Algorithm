import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque()
for n in range(N):
    n = sys.stdin.readline().split()
    n1= n[0] 
    if n1 == 'push':
        q.append(int(n[1]))
    elif n1 == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)

    elif n1 == 'size':
        print(len(q))

    elif n1 == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif n1 == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
        
    elif n1 == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
