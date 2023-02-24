import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
numbers = deque(list(map(int, sys.stdin.readline().split())))
Q = deque([ n for n in range(1,N+1)])
cnt = 0
while True:
    if len(Q) == N - M:
        break
    else:
        n = numbers[0]
        if Q[0] == n:
            Q.popleft()
            numbers.popleft()
        elif len(Q)//2 >= Q.index(n):   # 중간보다 앞쪽에 있다면
            Q.rotate(-1)    # 오른쪽으로 한 칸씩 rotate(1) 
            cnt += 1
        else:
            Q.rotate(1)
            cnt += 1
print(cnt)