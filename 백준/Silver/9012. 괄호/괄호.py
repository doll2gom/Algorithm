from collections import deque

l = []
# N입력
N = int(input())
for n in range(1, N + 1):
    # 문자열 입력
    S = deque(input())
    # 문자열 갯수가 1개 남을 때까지 S문자열 반복 
    while True:
        for s in list(S):
            if s == '(':
                l.append(S.popleft())
            elif s == ')':
                if '(' in l:
                    S.popleft()
                    l.pop(0)
                else:
                    break
        break
    # S문자열과 l리스트 모두 비어있다면 YES 아니면 NO
    if len(S) == 0 and len(l) == 0:
        print('YES')
    else:
        print('NO')
    l.clear()