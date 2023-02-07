dots = int(input())  # 정점의 수
line = int(input()) # 간선의 수

# 그래프 표현 방법1
# 인접 리스트
# 리스트 수는 노드의 수(dots)
# dots+1 만큼 리스트를 가진 리스트
graph = []
for _ in range(dots+1):
    graph.append([])


#정점의 쌍 입력(line 간선만큼)
for l in range(line):
    dot1, dot2 = list(map(int, input().split()))
    
    # 양방향 그래프
    # dot1의 인접리스트에 dot2를 추가
    graph[dot1].append(dot2)

    # dot2의 인접리스트에 dot1를 추가
    graph[dot2].append(dot1)
    # print(graph)

### 템플릿 1
# 시작점
# 1) 문제에서 주어지는 경우
# 2) 탐색을 해서 찾는 경우
start = 1

### 템플릿 2
# 스택(방문할(=탐색할)정점을 넣을)
# 방문여부 확인 변수
stack = []

# 방문여부를 확인할 변수
# visit = [False] * (dots +1)

# 중복을 확인할 때 사용하는 자료구조?
# set 데이터 타입을 활용해서 방문 여부를 확인 가능
# set의 시간복잡도 = O(1)
visit = set()

### 템플릿 3
# 스택에 시작점을 놓음
stack.append(start)
# 시작점 방문 표시
visit.add(start)

### 템플릿 5-3-3
# 방문한 횟수
visit_count = 0

### 템플릿 4
# 스택의 길이가 0이 아니면 무한반복
while len(stack) !=0:

    # 템플릿 5-1
    # stack에서 값을 꺼낸다.
    # 현재 내가 보고 있는 노드이자 현재 보는 컴퓨터이자 dot을 
    # current_dot = 지금 위치 노드
    current_dot = stack.pop()

    # 템플릿 5-2
    # 인접 정점을 확인한다. 
    # 양방향을 표현한 graph에서 현재 노드의 인접한 노드의 리스트를 가져온다. 
    # grap = 방문한 노드 목록
    adj_graph = graph[current_dot]

    # 템플릿 5-3 
    # adj_graph에서 인접 노드 중에 미방문한 노드
    for dot in adj_graph:

        # set을 활용한 방문했는지 안 했는지 확인
        # 현재 위치한 인접 정점이 방문변수(visit)에 없으면
        # 미방문 확인
        if dot not in visit:

            # 템플릿 5-3-1
            # stack에 인접 정점을 추가
            stack.append(dot)

            # 템플릿 5-3-2 
            # 템플릿 3 확인
            visit.add(dot)

            # 템플릿 5-3-3
            # 방문한 횟수 + 1
            visit_count += 1
            
print(visit_count)