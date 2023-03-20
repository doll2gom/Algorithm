import sys
scores = list(map(int, sys.stdin.readline().split()))
myscore = int(sys.stdin.readline())
if myscore in scores[0:5]:
    print('A+')
elif myscore in scores[5:15]:
    print('A0')
elif myscore in scores[15:30]:
    print('B+')
elif myscore in scores[30:35]:
    print('B0')
elif myscore in scores[35:45]:
    print('C+')
elif myscore in scores[45:48]:
    print('C0')
else:
    print('F')