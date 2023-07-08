import sys
T = int(sys.stdin.readline())
stack = []
ans = []
tf = True
cnt = 1
for t in range(1, T+1):
    n = int(sys.stdin.readline())
    while cnt <= n:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    if stack[-1] == n:
        stack.pop()
        ans.append('-')
    else:
        tf = False
        break
        
if tf == False:
    print('NO')
else:
    for i in ans:
        print(i)
