x = int(input())
N = int(input())
A = 0
for n in range(N):
    a, b = input().split()
    A += int(a)*int(b)
if x == A:
    print("Yes")
else:
    print("No")