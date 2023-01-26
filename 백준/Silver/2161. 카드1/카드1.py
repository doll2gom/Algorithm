# N입력
N = int(input())

# q1 = [i for i in range(1,N+1)]
q2 = list(range(1,N+1))
dis_q = []
# 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.
# == > 1장 남을 때까지 반복while
while len(q2) > 1:
    # 우선 제일 위에 있는 카드 버림
    # q2에서 제일 위 : pop(0)
    dis_q.append(q2.pop(0))
    # 버린 리스트에서 제일 위에 있는 카드를 제일 밑으로
    q2.append(q2.pop(0))
print(*dis_q, *q2)