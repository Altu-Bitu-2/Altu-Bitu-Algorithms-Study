import sys
import heapq as hq
input = sys.stdin.readline

def solution():
    n = int(input())
    max_heap = []
    for _ in range(n):
        line = input().strip()
        # 아이들 선물 나누기
        if line == "0": 
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(-1)
        # 선물 충전
        else: 
            gifts = list(map(int, line.split()))
            for g in gifts[1:]:
                hq.heappush(max_heap, -g)

if __name__ == "__main__":
    solution()