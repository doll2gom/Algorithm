S_dict = dict(zip(['b', 'd', 'p', 'q'],['d', 'b', 'q', 'p']))
lst = []

T = int(input())
for test_case in range(1, T+1):
    #테스트 케이스 숫자 입력
    S = input()
    for s in S:
        lst.append(S_dict[s])
    lst.reverse()
    print(f'#{test_case} ', *lst, sep='')
    lst = []