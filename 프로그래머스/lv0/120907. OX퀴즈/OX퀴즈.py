def solution(quiz):
    answer = []
    for q in quiz:
        q = list(map(str, q.split()))
        q0 = int(q[0])
        q2 = int(q[2])
        q4 = int(q[4])
        if q[1] == '-':
            if q0 - q2 == q4:
                answer.append("O")
            else:
                answer.append("X") 
        else:
            if q0 + q2 == q4:
                answer.append("O")
            else:
                answer.append("X") 
    return answer