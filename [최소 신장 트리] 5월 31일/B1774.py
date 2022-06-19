import sys, math
import heapq as hq
from itertools import combinations
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
    parents[px] += parents[py]
    parents[py] = px
    return True
    
def calculate_distances():
    distances = []
    
    for a, b in combinations([i for i in range(n)], 2):
        if find_parent(a) == find_parent(b): continue # 이미 연결됨
        dist = math.sqrt(math.pow(coordinates[a][0] - coordinates[b][0], 2) + math.pow(coordinates[a][1] - coordinates[b][1], 2))
        hq.heappush(distances, (dist, a, b))
    
    return distances

def solution(k):
    distances = calculate_distances()
    cost = 0
    
    while k > 0:
        dist, a, b = hq.heappop(distances)
        if union_parent(a, b):
            k -= 1
            cost += dist
            
    return cost
            
if __name__ == "__main__":
    n, m = map(int, input().split()) # 신 수, 이미 연결된 통로 개수
    coordinates = [tuple(map(int, input().split())) for _ in range(n)] # 신 좌표
    
    k = n - 1 # 필요한 통로 개수
    
    parents = [-1] * n
    for _ in range(m):
        a, b = map(int, input().split())
        if union_parent(a-1, b-1): k -= 1
        
    print(format(solution(k), ".2f"))
    