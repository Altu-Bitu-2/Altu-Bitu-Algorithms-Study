import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start, destination):
    
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    hq.heappush(q, (0, start))
    
    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist: continue # 이미 갱신됨
        for cost, next in graph[now]:
            tmp = dist + cost
            if distance[next] > tmp:
                distance[next] = tmp
                hq.heappush(q, (tmp, next))

    return distance[destination]

def specific_shortest_path():
    path_0 = dijkstra(1, v2) + dijkstra(v1, n) # 1 -> v2 -> v1 -> n
    path_1 = dijkstra(1, v1) + dijkstra(v2, n) # 1 -> v2 -> v1 -> n
    answer = min(path_0, path_1) + dijkstra(v1, v2)
    
    return answer if answer < INF else -1

if __name__ == "__main__":
    INF = int(1e9)
    
    n, e = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    v1, v2 = map(int, input().split())
    
    print(specific_shortest_path())