from collections import deque
import sys
input = sys.stdin.readline


def update_parts(parts, next, now):
    amount = parts[next][now]
    parts[next][now] = 0
    
    for i, val in enumerate(parts[now]):
        if val == 0: continue
        parts[next][i] += amount * val

def topological_sort(n, indegree, graph, parts):
    d = deque()

    for i in range(n):
        if indegree[i] == 0:
            d.append(i)
            parts[i][i] = 1

    while d:
        now = d.popleft()
        for next in graph[now]:            
            indegree[next] -= 1
            update_parts(parts, next, now) # 연결되어 있는 노드에 대해 업데이트
            if indegree[next] == 0: # 선행되는 노드 모두 확인
                d.append(next)

    return [f"{i+1} {val}" for i, val in enumerate(parts[n-1]) if val != 0]

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    indegree = [0] * n
    graph = [[] for _ in range(n)]
    parts = [[0] * n for _ in range(n)]
    
    for _ in range(m):
        x, y, k = map(int, input().split())
        # 완제품 x를 만드는데 중간 부붐 혹은 기본 부품 y가 k개 필요
        parts[x-1][y-1] = k 
        indegree[x-1] += 1
        graph[y-1].append(x-1) # 다음 노드
    
    print("\n".join(topological_sort(n, indegree, graph, parts)))