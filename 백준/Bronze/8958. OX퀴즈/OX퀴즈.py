lst = []
T = int(input())
for t in range(T):
    t = str(input())
    cnt = 0
    ans = 0
    for result in t:
        if result == 'O':
            cnt += 1
            ans += cnt
        elif result == 'X':
            cnt = 0
    print(ans)