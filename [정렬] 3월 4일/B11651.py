import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    # dots = []
    
    # for _ in range(n):
    #     x, y = map(int, input().split())
    #     dots.append((x, y))
    
    dots = [tuple(map(int, input().split())) for _ in range(n)]
    
    dots.sort(key=lambda x: (x[1], x[0]))
    
    for x, y in dots:
        print(x, y)
    
if __name__ == "__main__":
    solution()