import sys
num = int(sys.stdin.readline())
random = list(map(int,sys.stdin.readline().split()))
lst = []
for i in range(1, num+1):
    lst.insert(random[i-1],i)
lst = reversed(lst)
print(*lst)
