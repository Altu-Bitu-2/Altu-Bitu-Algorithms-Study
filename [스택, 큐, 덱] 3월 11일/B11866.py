import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    
    d = deque([i for i in range(1, n+1)])
    ans = []
    cnt = 0
    while d:
        num = d.popleft()
        cnt += 1
        if cnt == k:
            cnt = 0
            ans.append(num)
        else:
            d.append(num)
    
    print("<", end="")
    for i in range(n):
        print(ans[i], end="")
        if i != n-1:
            print(", ", end="")
    print(">")

if __name__ == "__main__":
    solution()