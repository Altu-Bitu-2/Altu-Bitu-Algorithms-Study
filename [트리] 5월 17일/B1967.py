import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def get_tree_diameter(n, tree):
    if n == 1: return 0
    # 시작 노드에서 가장 먼 노드를 찾는 함수
    def find_furtest_node(start):
        
        def dfs(now, dist):
            nonlocal max_node, max_value
            
            for next, weight in tree[now]:
                if dist[next] == -1: # 방문하지 않은 노드
                    distance = weight + dist[now] # 거리 계산
                    dist[next] = distance # 거리 갱신
                    if distance > max_value: # 최대 거리 찾기
                        max_node = next
                        max_value = distance
                    dfs(next, dist)
                    
        # 시작 노드에서의 거리
        dist = [-1] * (n + 1)
        dist[start] = 0
        max_node, max_value = -1, -1 # 가장 먼 노드, 거리
        dfs(start, dist) # dfs로 시작 노드에서 가장 먼 노드와 거리 찾기
        
        return max_node, max_value
    
    start, _ = find_furtest_node(1)
    _, result = find_furtest_node(start)
    
    return result

if __name__ == "__main__":
    n = int(input())
    
    # 루트 노드: 1
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        p, c, w = map(int, input().split())
        tree[p].append((c, w))
        tree[c].append((p, w))
        
    print(get_tree_diameter(n, tree))