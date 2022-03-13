import sys
input = sys.stdin.readline

def solution():
    s = input().strip()
    
    results = {s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)}
    
    print(len(results))

if __name__ == "__main__":
    solution()