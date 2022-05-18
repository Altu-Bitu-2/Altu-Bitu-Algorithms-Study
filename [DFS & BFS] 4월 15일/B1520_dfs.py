import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == m - 1 and y == n - 1: return 1
    if dp[x][y] != -1: return dp[x][y] # 방문한 적 있는 점
    
    # 방문한 적 없는 점
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
        if graph[nx][ny] >= graph[x][y]: continue
        dp[x][y] += dfs(nx, ny) # 이전까지의 경로의 합
            
    return dp[x][y]

if __name__ == "__main__":
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    dp = [[-1] * n for _ in range(m)]
    
    print(dfs(0, 0))