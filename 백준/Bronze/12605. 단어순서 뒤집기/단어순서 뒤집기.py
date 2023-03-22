import sys
N = int(sys.stdin.readline())
for case in range(1, N+1):
    n = reversed(list(map(str, sys.stdin.readline().split())))
    print(f'Case #{case}: {" ".join(n)}')