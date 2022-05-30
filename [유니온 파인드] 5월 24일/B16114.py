import sys
input = sys.stdin.readline

def solution():
    if n != 1 and n % 2 == 1: return "ERROR"
    if (n == 0 and x > 0) or (n == 1 and x < 0): return "INFINITE"
    
    offset = n//2
    if n != 1 and x > 0: return ((x + offset - 1) // offset - 1)
    else: return 0
    
if __name__ == "__main__":
    x, n = map(int, input().split())
    print(solution())