from itertools import permutations

N, M = list(map(int, input().split()))
lst = [num for num in range(1, N+1)]

a = permutations(lst, M)
for a2 in a:
    print(*a2, sep =' ')

