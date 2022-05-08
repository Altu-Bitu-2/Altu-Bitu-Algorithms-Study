#  N과 M (7)
import sys
input = sys.stdin.readline

def backtracking():
    if len(l) == m:
        print(" ".join(map(str, l)))
        return
    
    for i in range(n):
        l.append(numbers[i])
        backtracking()
        l.pop()
        
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()
    
    l = []
    backtracking()