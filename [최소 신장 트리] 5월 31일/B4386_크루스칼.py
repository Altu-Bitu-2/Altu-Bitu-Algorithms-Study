# 크루스칼
import sys, math
from itertools import combinations
import heapq as hq
input = sys.stdin.readline

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

def calculate_distances():    
    for a, b in combinations([i for i in range(n)], 2):
        dist = math.sqrt(math.pow(stars[a][0] - stars[b][0], 2) + math.pow(stars[a][1] - stars[b][1], 2))
        hq.heappush(distances, (dist, a, b))

def kruskal():
    calculate_distances()
    cost = 0
    count = 0
    while (count < n - 1):
        dist, a, b = hq.heappop(distances)
        if union_parent(a, b):
            count += 1
            cost += dist
    return cost

if __name__ == "__main__":
    n = int(input())
    stars = [tuple(map(float, input().split())) for _ in range(n)]
    distances = []
    parents = [-1] * n
    print(f"{kruskal():.3}")