import sys
import heapq as hq
input = sys.stdin.readline

def solution():
    k = int(input())
    files = list(map(int, input().split()))
    
    hq.heapify(files)
    
    total = 0
    while len(files) > 1:
        x1 = hq.heappop(files)
        x2 = hq.heappop(files)
        total += x1 + x2
        hq.heappush(files, x1 + x2)
    
    print(total)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solution()