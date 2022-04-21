import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    belief = [-1] * (n + 1) # 믿기 시작한 시간
    
    q = deque()
    for start in starts:
        q.append((start, 0))
    
    while q:
        now, time = q.popleft()
        if belief[now] != -1: continue # 같은 시간에 믿고, 이웃인 사람이 있을 경우
        belief[now] = time
        
        # 주변 사람 믿을지 확인
        for next in neighbors[now]: 
            if belief[next] != -1: continue # 벌써 믿고 있는 경우
            total = len(neighbors[next])
            cnt = sum([1 for nb in neighbors[next] if belief[nb] >= 0])
            if total <= cnt * 2: # 과반수가 믿는 경우
                # 같은 시간에 믿을 이웃들을 제외하고, 과거에 믿었던 이웃만 고려하기 위해
                # belief 값을 갱신하는 대신 큐에 시간을 넣기
                q.append((next, belief[now] + 1)) 
    
    return belief[1:]

if __name__ == "__main__":
    n = int(input())
    neighbors = [list(map(int, input().split()))[:-1] for _ in range(n)]
    neighbors = [[]] + neighbors
    
    m = int(input())
    starts = list(map(int, input().split()))
    
    print(" ".join(map(str, bfs())))