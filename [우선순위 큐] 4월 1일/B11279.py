import sys
import heapq as hq
input = sys.stdin.readline

def solution():
    n = int(input())
    max_heap = []
    
    for _ in range(n):
        x = int(input()) 
        if x:
            hq.heappush(max_heap, -x)
        else:
            if len(max_heap):
                print(-hq.heappop(max_heap))
            else:
                print(0)

if __name__=="__main__":
    solution()