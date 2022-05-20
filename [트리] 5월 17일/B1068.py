import sys
from collections import deque
input = sys.stdin.readline

def count_leaves(n, parents):
    # 삭제되지 않았고, 리프노드인 것 카운트
    return len([i for i in range(n) if parents[i] != -2 and i not in set(parents)])

def remove_node(target, parents):
    q = deque()
    q.append(target)
    parents[target] = -2
    
    while(q):
        now = q.popleft()
        for i in range(n):
            if parents[i] == now:
                q.append(i)
                parents[i] = -2
    
if __name__ == "__main__":
    n = int(input())
    parents = list(map(int, input().split()))
    target = int(input())
    remove_node(target, parents)
    print(count_leaves(n, parents))