cnt = 0
A = list(map(int, input().split()))
for n in A:
    aa = n*n
    cnt += aa
print(cnt%10)