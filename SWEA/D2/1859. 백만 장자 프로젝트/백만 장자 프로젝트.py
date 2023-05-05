T = int(input())
for t in range(1, T+1):
    _ = int(input())
    lst = list(map(int, input().split()))
    max = lst[-1]
    ans = 0
    for n in lst[::-1]:
        if n >= max:
            max = n
        else:
            ans += (max - n)
    print(f'#{t} {ans}')