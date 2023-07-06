import sys
T = int(sys.stdin.readline())
for t in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    floor0 = [ a for a in range(1, n+1)] # 0번 층 리스트 만들기 
    for kk in range(k):
        for nn in range(1, n):
            floor0[nn] += floor0[nn-1]
        # print(floor0)
    print(floor0[-1])
            