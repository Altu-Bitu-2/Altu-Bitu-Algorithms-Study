#  N과 M (1)
import sys
input = sys.stdin.readline

def backtracking(now):
    if len(l) == m:
        print(" ".join(map(str, l)))
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        l.append(i)
        backtracking(i+1)
        l.pop()
        visited[i] = False
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    l = []
    visited = [False] * (n+1)
    backtracking(1)