N, K = map(int,input(). split())
K2 = K
lst = [ i for i in range(1,int(N)+1)]
lst2 = []
a = []
idx = 0
'''
@comment
K의 값을 미리 1 빼둠
아래 코멘트 참조
'''
K -= 1
while True: 
    cnt = 0
    '''
    @comment
    for k in lst[K-1::K2]은 매 루프마다 K를 계속 -1 해서 계산해야 하기 때문에
    K를 미리 1을 빼고 시작
    '''
    for k in lst[K::K2]:    
        a.append(k)
        cnt += 1
    idx2 = idx
    for mem in a[idx2:]:
        lst.remove(mem)
        idx += 1
        
    if not lst:
        break
    '''
    @comment
    K가 가르킬 다음 인덱스는 K위치를 포함해 K2번째, 즉 K + K2 - 1인데
    K2를 더하는 것과 1을 빼는 것이 cnt만큼 반복되므로 (K2-1) * cnt
    '''
    K = (K + (K2-1) * cnt) % len(lst)
print('<', end = '')
print(*a, sep = ', ', end = '')
print('>', end = '')