import heapq
import sys
n = int(sys.stdin.readline())
my = int(sys.stdin.readline())
cnt = 0
h = []
for i in range(n-1):
    heapq.heappush(h, -int(sys.stdin.readline()))
    
while True:
    if n == 1:
        break
    vote = heapq.heappop(h)
    if my <= -vote:
        my += 1
        cnt += 1
        heapq.heappush(h, vote + 1)
    else:
        break
print(cnt)