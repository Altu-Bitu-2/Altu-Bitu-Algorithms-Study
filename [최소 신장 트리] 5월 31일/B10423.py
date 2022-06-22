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
    if px in plants and py in plants: return False # 둘다 발전소에 연결되어 있음
    
    if parents[px] > parents[py]: px, py = py, px # 노드 개수가 더 작은 루트노드가 px
    if py in plants: px, py = py, px # 발전소라면 px
    
    parents[px] += parents[py]
    parents[py] = px
    return True

def solution():
    answer = 0
    count = n - k
    while count > 0:
        cost, u, v = hq.heappop(costs)
        if union(u, v):
            answer += cost 
            count -= 1

    return answer   
        
if __name__ == "__main__":
    n, m, k = map(int, input().split()) # 도시 개수, 설치 가능 케이블 수, 발전소 개수
    # 케이블설치 비용 최소, 모든 도시 전기 공급
    # 케이블 연결 도시에 발전소 반드시 하나만 존재
    
    parents = [-1] * (n + 1)
    plants = set(map(int, input().split())) # 발전소
    
    costs = []
    for _ in range(m): # 두 도시를 연결하는 케이블 정보
        u, v, w = map(int, input().split()) # u, v 도시, w 비용
        hq.heappush(costs, (w, u, v))
    
    print(solution())