import sys
for _ in range(int(sys.stdin.readline())):
    a, b = 0, 0
    for _ in range(int(sys.stdin.readline())):
        name, num = sys.stdin.readline().split()
        num = int(num)
        if b < num:
            a, b = name, num
        else:
            pass
    print(a)