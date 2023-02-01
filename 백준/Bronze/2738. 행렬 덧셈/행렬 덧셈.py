N, M = map(int, input().split())
A = [ list(map(int, input().split())) for i in range(N)]
B = [ list(map(int, input().split())) for i in range(N)]
matrix = [ [ None for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        matrix[i][j] = A[i][j] + B[i][j]
    print(*matrix[i])