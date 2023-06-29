n = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
ans = sorted(a - b)
print(len(ans))
if len(ans) != 0:
    print(*ans)