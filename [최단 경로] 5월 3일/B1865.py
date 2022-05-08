import sys
input = sys.stdin.readline

# 음의 사이클 존재하는지 확인
def bellmanford():
    distance = [INF] * (n+1)
    
    # n번 반복
    for i in range(n):
        # 모든 간선 확인
        for now in range(1, n+1):
            for cost, next in graph[now]:
                tmp = distance[now] + cost
                if distance[next] > tmp:
                    # n번째 반복에서 거리 정보 갱신 시, 음의 사이클 발생
                    if i == n-1: return True
                    distance[next] = tmp
                     
    return False

def has_negative_cycles():
    return "YES" if bellmanford() else "NO"

if __name__ == "__main__":
    INF = int(1e9)
    t = int(input())
    for _ in range(t):
        n, m, w = map(int, input().split())
        
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            s, e, t = map(int, input().split())
            graph[s].append((t, e))
            graph[e].append((t, s))
            
        for _ in range(w):
            s, e, t = map(int, input().split())
            graph[s].append((-t, e))
            
        print(has_negative_cycles())