import heapq as hq
import sys
input = sys.stdin.readline

def topological_sort(n, graph, indegree):
    min_heap = [] # 작은 값부터 출력

    for i in range(n):
        if indegree[i] == 0:
            hq.heappush(min_heap, i)
    
    while min_heap:
        now = hq.heappop(min_heap)
        print(now+1, end = " ")
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0: hq.heappush(min_heap, next)

if __name__ == "__main__":
    n, m = map(int, input().split()) # 문제 수, 정보 개수
    
    indegree = [0] * n # 진입 차수
    graph = [[] for _ in range(n)] # 연결 그래프
    
    for _ in range(m):
        a, b = map(int, input().split()) # a는 b보다 먼저 풀어야 함
        indegree[b-1] += 1
        graph[a-1].append(b-1) 
        
    topological_sort(n, graph, indegree)