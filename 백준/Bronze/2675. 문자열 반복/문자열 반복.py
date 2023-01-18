QR = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:'
T = int(input())
for t in range(0,T):
    R, S = input().split()
    R = int(R)
    S = str(S)
    for r in S[:]:
        if r in QR:
            print(r*R,end='')
    print()