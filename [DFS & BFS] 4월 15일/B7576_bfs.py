import sys
from collections import deque
input = sys.stdin.readline

def check_status(graph):
    ans = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1 # 익지 않은 토마토 있음
            ans = max(ans, graph[i][j])
    return ans - 1

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1: continue
            if graph[nx][ny]: continue # 빈 칸, 익은 토마토
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))
    
def solution():
    if check_status(graph) != -1: return 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1: 
                q.append((i, j))
    bfs()
                
    return check_status(graph)

if __name__ == "__main__":
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    q = deque()
    
    print(solution())
    
        