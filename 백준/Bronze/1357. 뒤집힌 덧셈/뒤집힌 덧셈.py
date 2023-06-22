a, b = input().split()
c = str(int(a[::-1]) + int(b[::-1]))[::-1]
print(int(c))
