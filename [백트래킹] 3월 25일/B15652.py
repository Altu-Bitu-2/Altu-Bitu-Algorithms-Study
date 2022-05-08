#  N과 M (4)
import sys
input = sys.stdin.readline

def backtracking(now):
    if len(l) == m:
        print(" ".join(map(str, l)))
        return
    
    for i in range(now, n+1):        
        l.append(i)
        backtracking(i)
        l.pop()
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    l = []
    backtracking(1)