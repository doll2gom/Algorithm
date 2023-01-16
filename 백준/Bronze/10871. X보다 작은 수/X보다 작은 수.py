N, X = map(int,input().split())
A = list(map(int,input().split()))
for n in A[0:N+1]:
    if n >= X:
        A.remove(n)
    else:
        print(n, end=' ')