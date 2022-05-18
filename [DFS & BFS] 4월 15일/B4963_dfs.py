import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 런타임 에러(RecursionError) 방지

def dfs(x, y):
    # 가로, 세로, 대각선
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    
    graph[x][y] = 0 # 방문 처리
    
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= h or ny >= w: continue # 지도 범위 벗어난 경우
        if graph[nx][ny] == 0: continue # 바다이거나 방문한 땅인 경우
        dfs(nx, ny)

if __name__ == "__main__":
    # 1: 땅, 0: 바다
    # w, h : 1, 2, ..., 50
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0: break # 입력 끝
            
        graph = [list(map(int, input().split())) for _ in range(h)]
        
        ans = 0 
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1: # 방문하지 않은 땅
                    dfs(i, j)
                    ans += 1 # 섬의 개수 1 증가
        print(ans)