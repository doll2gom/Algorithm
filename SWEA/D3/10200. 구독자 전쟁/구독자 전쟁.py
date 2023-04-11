T = int(input())
for t in range(1, T+1):
    n, a, b = map(int, input().split())
    if n <= a + b: # 7 5
        Min = (a + b) - n
        Max = min(a, b)
    else: # 3 5
        Min = 0
        Max = min(a, b)
    print(f'#{t} {Max} {Min}')