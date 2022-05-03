import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    count_houses = 1 # 각 단지 당 집 개수    
    q = deque() # 큐
    q.append((x, y))
    graph[x][y] = '0' # 방문 표시
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if graph[nx][ny] == '1':
                q.append((nx, ny))
                count_houses += 1 # 집 수 1 증가
                graph[nx][ny] = '0' # 방문 표시
                
    return count_houses
                
# 단지 내 집 개수를 원소로하는 배열 반환하는 함수
def count_houses_in_complex():
    complexes = []
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1':
                complexes.append(bfs(i, j))
    
    return sorted(complexes) # 오름차순 정렬

if __name__ == "__main__":
    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]
    
    complexes = count_houses_in_complex()
    print(len(complexes))
    print("\n".join(map(str, complexes)))