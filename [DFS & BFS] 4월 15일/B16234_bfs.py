import sys
from collections import deque
input = sys.stdin.readline

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 연합을 이루고 있는 각 칸의 인구수 갱신
def change_val(union, people):
    val = people // len(union)
    for x, y in union: arr[x][y] = val

# 시작 칸을 포함하는 연합 찾기
def bfs(start_x, start_y, visited):
    
    # 연합 찾기
    people = 0 # 연합 인구수
    union = [] # 연합을 이루고 있는 칸 저장
    q = deque()
    
    q.append((start_x, start_y))
    visited[start_x][start_y] = True
    
    while q:
        x, y = q.pop()
        union.append((x, y))
        people += arr[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1: continue
            if visited[nx][ny]: continue
            if l <= abs(arr[nx][ny] - arr[x][y]) <= r: # 국경선 공유
                visited[nx][ny] = True
                q.append((nx, ny))
    
    # 연합 인구수 갱신
    change_val(union, people)

def move():
    days = 0 # 인구 이동 일수
    
    while True:
        # 하루동안 인구 이동
        visited = [[False] * n for _ in range(n)]
        count = 0 # 연합 개수
        
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    bfs(i, j, visited)
                    count += 1
        
        # 모든 인구 이동 끝난 경우
        if count == n * n: return days
        # 하루 증가
        days += 1

if __name__ == "__main__":
    n, l, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(move())