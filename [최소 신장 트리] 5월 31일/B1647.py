import sys
import heapq as hq
input = sys.stdin.readline

# 두 개의 분리된 마을의 각각의 최소 신장 트리
# 최소 신장 트리 하나 만들기 -> 가장 큰 가중치의 간선 없애기

def find_parent(x):
    if parents[x] < 0: return x
    parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    px = find_parent(x)
    py = find_parent(y)
    if px == py: return False
    
    if parents[px] > parents[py]: px, py = py, px 
    # px의 집합 노드 수 >= py의 집합 노드 수
    parents[px] += parents[py]
    parents[py] = px
    return True

def kruskal():
    total = 0
    count = 0
    max_cost = 0
    while count < n-1:
        cost, a, b = hq.heappop(graph)
        if union_parent(a, b):
            count += 1
            max_cost = max(cost, max_cost)
            total += cost
    return total - max_cost            
        
if __name__ == "__main__":
    n, m = map(int, input().split()) # 집의 개수, 길의 개수
    parents = [-1] * (n+1)
    graph = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        hq.heappush(graph, (c, a, b))
        
    print(kruskal())