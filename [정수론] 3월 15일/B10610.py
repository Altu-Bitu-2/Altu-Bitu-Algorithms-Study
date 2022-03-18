import sys
input = sys.stdin.readline

def solution():
    n = input().strip()
    
    if sum(map(int, n)) % 3 != 0 or '0' not in n:
        print("-1")
        return
    
    result = sorted(list(n), reverse=True)
    print("".join(result))
    
if __name__ == "__main__":
    solution()