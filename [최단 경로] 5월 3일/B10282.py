import sys
import heapq as hq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    distance = [INF] * (n+1)
    
    hq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = hq.heappop(q)
        if distance[now] < dist: continue # 이미 갱신됨
        for cost, next in graph[now]:
            tmp = dist + cost
            if distance[next] > tmp:
                distance[next] = tmp
                hq.heappush(q, (tmp, next))
    
    return distance

def calculate_infection():
    count, time = 0, 0
    distance = dijkstra(c)
    for d in distance:
        if d < INF:
            count +=1
            time = max(time, d)
    return count, time            

if __name__ == "__main__":
    INF = int(1e9)
    t = int(input())
    for _ in range(t):
        n, d, c = map(int, input().split())

        # 의존성
        graph = [[] for _ in range(n+1)]
        for _ in range(d):
            a, b, s = map(int, input().split())
            graph[b].append((s, a))
            
        print(" ".join(map(str, calculate_infection())))
    