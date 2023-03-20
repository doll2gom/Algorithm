import sys
T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    cnt_c, cnt_g = 0, 0
    for n in range(N):
        lst = sys.stdin.readline().split()
        cnt_c += int(lst[0])
        cnt_g += float(lst[0]) * float(lst[1])
    print(cnt_c, "{0:.1f}".format(cnt_g/cnt_c))