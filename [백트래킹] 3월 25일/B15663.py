#  N과 M (9)
import sys
input = sys.stdin.readline

def backtracking():
    if len(l) == m:
        print(" ".join(map(str, l)))
        return
    
    pre = -1
    for i in range(n):
        if visited[i]: continue
        if pre == numbers[i]: continue
        pre = numbers[i]
                
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