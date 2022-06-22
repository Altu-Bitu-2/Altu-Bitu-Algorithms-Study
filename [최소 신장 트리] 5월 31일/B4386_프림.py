# 프림
import sys
import heapq as hq
input = sys.stdin.readline
        
def prim(start):
    result = 0
    pq = []
    visited = [False] * n # 정점 방문 여부
    distances = [INF] * n # 각 정점에서 선택한 간선의 가중치

    distances[start] = 0
    hq.heappush(pq, (0, start))
    
    while pq:
        cost, now = hq.heappop(pq)
        if visited[now]: continue # 이미 확인한 정점
        visited[now] = True # 방문 처리
        result += cost
        for next_cost, next in graph[now]:
            if not visited[next] and next_cost < distances[next]:
                hq.heappush(pq, (next_cost, next))
                distances[next] = next_cost
    return result

if __name__ == "__main__":
    INF = int(1e5)
    n = int(input())
    graph = [[] for _ in range(n)]
    stars = []
    for i in range(n):
        x, y = map(float, input().split())
        for j in range(i):
            dist = ((stars[j][0] - x) ** 2 + (stars[j][1] - y) ** 2) ** 0.5
            graph[i].append((dist, j))
            graph[j].append((dist, i))
        stars.append((x, y))
    
    print(f"{prim(0):.3}")