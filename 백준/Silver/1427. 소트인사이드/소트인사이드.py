import sys
N = sys.stdin.readline()
lst = []
for n in N:
    lst.append(n)
print(*reversed(sorted(lst)), sep='', end='')