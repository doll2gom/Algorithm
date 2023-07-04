import sys
N, P = map(int, sys.stdin.readline().split())
cnt = 0
lst = [ map(int, sys.stdin.readline().split()) for _ in range(N)]
lst2 = [[] for _ in range(7)]

for i, j in lst:
    if not lst2[i]:
        lst2[i].append(j) # i번 줄 j번 프렛에 손가락을 누른다
        cnt += 1
    else:
        if lst2[i][-1] < j:
            lst2[i].append(j) # i번 줄 j번 프렛에 손가락을 누른다
            cnt += 1
        elif lst2[i][-1] == j: 
            continue
        else:
            # i번 줄에 손가락을 누르고 있는 프렛을 뒤에서부터 탐색
            for jj in range(len(lst2[i])-1, -1, -1):
                if lst2[i][jj] < j:
                    lst2[i].append(j) # i번 줄 j번 프렛에 손가락을 누른다
                    cnt += 1
                    break
                elif lst2[i][jj] > j:
                    lst2[i].pop() # i번 줄 마지막 프렛에서 손가락을 뗀다
                    cnt += 1
                else:
                    break
            if not lst2[i]:
                lst2[i].append(j) # i번 줄 j번 프렛에 손가락을 누른다
                cnt += 1
print(cnt)