import sys
sys.setrecursionlimit(1000000)
N, E = map(int, sys.stdin.readline().split())
graph = [ [] for _ in range(N+1)]
visited = []
cnt = 0

def dfs(n):
    visited.append(n)
    for n in graph[n]:
        if n not in visited:
            dfs(n)

for _ in range(E):
    u, v = map(int, sys.stdin.readline().split()) 
    graph[u].append(v)
    graph[v].append(u)


for n in range(1, N+1): 
    if n not in visited:
        dfs(n)
        cnt += 1
print(cnt)
