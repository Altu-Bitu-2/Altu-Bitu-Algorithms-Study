import sys
import heapq as hq
input = sys.stdin.readline

def solution():
    n = int(input())
    abs_heap = []
    for _ in range(n):
        x = int(input())
        if x:
            hq.heappush(abs_heap, (abs(x), x))
        else:
            if len(abs_heap):
                print(hq.heappop(abs_heap)[1])
            else:
                print(0)

if __name__ == "__main__":
    solution()