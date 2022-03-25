import sys, math
input = sys.stdin.readline
            
def solution():
    r, b = map(int, input().split())
    
    p = r + b
    s = r // 2 + 2
    
    d = int(math.sqrt(s * s - 4 * p))
    print((s + d)//2, (s - d)//2)
    
if __name__ == "__main__":
    solution()