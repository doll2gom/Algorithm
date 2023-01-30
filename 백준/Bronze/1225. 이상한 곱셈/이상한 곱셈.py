A, B = list(map(str,input().split()))
A = [int(a) for a in A]
B = [int(b) for b in B]
print(sum(A)*sum(B))