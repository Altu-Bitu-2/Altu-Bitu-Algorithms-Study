import sys
from collections import deque
input = sys.stdin.readline

# 큐에 방문 위치 저장
# dist 배열에 방문 시간 저장
def bfs(n, k):
    M = 2 * max(n, k) # 34
    dist = [-1] * (M + 1) 
    q = deque()
    q.append(n)
    dist[n] = 0
    while q:
        now = q.popleft() # 5
        # 처음으로 k 지점 방문하면 탐색 종료
        if now == k: return dist[now]
        for next in (now - 1, now + 1, 2 * now): # 4, 6, 10
            if next < 0 or next > M: continue
            if dist[next] != -1: continue
            dist[next] = dist[now] + 1 # dist[4, 6, 10] = 1
            q.append(next)

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(bfs(n, k))
    
# N, K
# 걷기: X-1, X+1
# 순간이동: 2*X
# 가장 빠른 시간