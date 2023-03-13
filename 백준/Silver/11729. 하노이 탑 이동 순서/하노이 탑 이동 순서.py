import sys
def hanoi(N, a, b, c):
    if N == 1:
        print(a, b)
    else:
        hanoi(N -1, a, c, b)
        print(a, b)
        hanoi(N -1, c, b, a)

N = int(sys.stdin.readline())
print((2 ** N) - 1)
hanoi(N, "1", "3", "2")