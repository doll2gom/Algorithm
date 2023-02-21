import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque()
for n in range(N):
    command = sys.stdin.readline().split()  # 명령을 입력받는다
    cmd = command[0]

    if cmd[0:4] == 'push':
        if cmd[-1] == 't':          # push_front X    정수 X를 덱의 앞에 넣는다.
            Q.appendleft(int(command[1]))
        elif cmd[-1] == 'k':        # push_back X     정수 X를 덱의 뒤에 넣는다.
            Q.append(int(command[1]))

    elif cmd[0:3] == 'pop':
        if len(Q) != 0:
            if cmd[-1] == 't':      # pop_front       덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
                print(Q.popleft())
            elif cmd[-1] == 'k':    # pop_back        덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.
                print(Q.pop())
        else:
            print(-1)               # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

    elif cmd == 'size':             # size            덱에 들어있는 정수의 개수를 출력한다.
        print(len(Q))

    elif cmd == 'empty':            # empty           덱이 비어있으면 1을, 아니면 0을 출력한다.
        if len(Q) != 0:
            print(0)
        else:
            print(1)
            
    elif cmd == 'front':            # front           덱의 가장 앞에 있는 정수를 출력한다.
        if len(Q) != 0:
            print(Q[0])
        else:
            print(-1)               # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

    elif cmd == 'back':            # back            덱의 가장 뒤에 있는 정수를 출력한다.
        if len(Q) != 0:
            print(Q[-1])
        else:
            print(-1)               # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.