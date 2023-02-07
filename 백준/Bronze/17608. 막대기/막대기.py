import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
	stack.append(int(input()))
cnt = 1
last = stack[-1]
for n in reversed(range(N)):
	if stack[n] > last:
		cnt += 1
		last = stack.pop(n)
print(cnt)