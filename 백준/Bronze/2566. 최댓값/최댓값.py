num = 0
I = 0
J = 0
matrix = [ list(map(int, input().split())) for _ in range(9)]
for i in range(9):
    for j in range(9):
        if matrix[i][j] >= num:
            I = i
            J = j
            num = matrix[i][j]
print(num)
print(I+1, J+1)