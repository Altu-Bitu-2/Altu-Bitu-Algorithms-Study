import sys
from collections import deque
input = sys.stdin.readline

def dfs(now, visited):
    visited[now] = True
    print(now, end = ' ')
    for v in graph[now]:
        if not visited[v]:
            dfs(v, visited)

def bfs(s):
    visited = [False] * (n + 1)
    q = deque()
    visited[s] = True
    q.append(s)
    while q:
        now = q.popleft()
        print(now, end = ' ')
        for v in graph[now]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    
def solution():
    visited = [False] * (n + 1)
    dfs(v, visited)
    print()
    bfs(v)
    
    
if __name__ == "__main__":
    n, m, v = map(int, input().split())
    # 양방향 그래프, 연결 리스트
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, n+1):
        graph[i].sort()
        
    solution()
        