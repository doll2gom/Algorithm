import sys
from collections import deque
test_case = int(sys.stdin.readline())
for t in range(test_case):
    N, M = map(int, sys.stdin.readline().split())
    Q = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0
    # print(N, M, nq, m)
    while Q:
        mx = max(Q)
        fst = Q[0]
        if mx == fst:
            Q.popleft()
            M -= 1
            cnt += 1
            if M < 0:
                print(cnt)
                break
        elif mx != fst:
            Q.rotate(-1)
            M -= 1
            if M < 0:
                M = len(Q) -1
