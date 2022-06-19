from collections import deque
import sys
input = sys.stdin.readline

def topological_sort(n, indegree, time, graph):
    d = deque()
    dp = [0] * n

    for i in range(n):
        if indegree[i] == 0:
            d.append(i)
            dp[i] = time[i]
    
    while d:
        now = d.popleft()
        for next in graph[now]:
            # 선행 사건의 가장 긴 시간
            dp[next] = max(dp[next], dp[now] + time[next])    
            indegree[next] -= 1
            if indegree[next] == 0: d.append(next)

    return dp

if __name__ == "__main__":
    n = int(input())
    
    indegree = [] # 진입 차수
    time = [] # 각 건물 완성되기까지 걸리는 최소 시간
    graph = [[] for _ in range(n)] # 연결 그래프
    
    for i in range(n):
        building = list(map(int, input().split()[:-1]))
        indegree.append(len(building)-1)
        time.append(building[0])
        for ant in building[1:]: graph[ant-1].append(i) # 연결된 정점
    
    print("\n".join(map(str, topological_sort(n, indegree, time, graph))))