#  N과 M (5)
import sys
input = sys.stdin.readline

def backtracking():
    if len(l) == m:
        print(" ".join(map(str, l)))
        return
    
    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        l.append(numbers[i])
        backtracking()
        l.pop()
        visited[i] = False
        
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    l = []
    visited = [False] * n
    backtracking()