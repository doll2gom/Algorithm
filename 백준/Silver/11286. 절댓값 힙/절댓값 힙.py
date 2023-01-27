import sys
import heapq

N = int(sys.stdin.readline())
lst = []
min_lst = []
for _ in range(0,N):
    x = int(sys.stdin.readline())
    # x가 0이 아니라면 
    if x != 0:
        # x의 음수 양수 여부에 따라 다른list에 추가
        if x < 0:
            heapq.heappush(lst, (abs(x),x))
        else:
            heapq.heappush(lst, (abs(x),x))
    # x가 0이라면 
    else:
        # 음수 list에 값이 있다면/ 음수 list 마지막 값을 출력
        if lst:
            l = heapq.heappop(lst)
            print(l[1])
        # 두 list 모두 비어있다면/ 0을 출력
        else:
            print(0)