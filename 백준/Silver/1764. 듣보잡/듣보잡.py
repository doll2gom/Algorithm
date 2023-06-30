N, M = map(int, input().split())
a = set()
b = set()
for _ in range(N):
    a.add(input())
for _ in range(M):
    b.add(input())
lst = []
cnt = 0
for i in b:
    if i in a:
        cnt += 1
        lst.append(i)
print(cnt)
for i in sorted(lst):
    print(i)