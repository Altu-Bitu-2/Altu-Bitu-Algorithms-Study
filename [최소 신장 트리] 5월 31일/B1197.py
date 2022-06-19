# Kruskal Algorithm
import sys
import heapq as hq
input = sys.stdin.readline

def find_parent(x):
    if parents[x] < 0: return x
    parents[x] = find_parent(parents[x])
    return parents[x]

def union(x, y):
    px = find_parent(x)
    py = find_parent(y)
    if px == py: return False
    if parents[px] > parents[py]: px, py = py, px # 노드 개수가 더 작은 루트노드가 px
    parents[px] += parents[py]
    parents[py] = px
    return True

def minimum_spanning_tree():
    weight = 0
    count = 0
    while (count < v-1):
        c, a, b = hq.heappop(edges)
        if union(a, b):
            count += 1
            weight += c
    return weight

if __name__ == "__main__":
    v, e = map(int, input().split())
    parents = [-1] * (v+1)
    edges = []
    for _ in range(e):
        a, b, c = map(int, input().split()) 
        # a 정점, b 정점이 가중치 c 간선으로 연결되어 있음
        # c 음수 가능, 절대값 1,000,000 이하
        hq.heappush(edges, (c, a, b)) # 가중치 최소힙
    
    print(minimum_spanning_tree())