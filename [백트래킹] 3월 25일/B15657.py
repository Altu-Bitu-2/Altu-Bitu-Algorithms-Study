#  N과 M (8)
import sys
input = sys.stdin.readline

def backtracking(now):
    if len(l) == m:
        print(" ".join(map(str, l)))
        return
    
    for i in range(now, n):
        l.append(numbers[i])
        backtracking(i)
        l.pop()
        
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    l = []
    backtracking(0)