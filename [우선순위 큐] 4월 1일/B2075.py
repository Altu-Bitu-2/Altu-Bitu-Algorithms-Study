import sys
import heapq as hq
input = sys.stdin.readline

def solution():
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]
    max_heap = []
    
    for i in range(n):
        hq.heappush(max_heap, (-table[-1][i], n-1, i))
    
    cnt = 0
    while max_heap:
        cnt += 1
        val, x, y = hq.heappop(max_heap)
        if cnt == n: return -val
        if x: hq.heappush(max_heap, (-table[x-1][y], x-1, y))

if __name__ == "__main__":
    print(solution())