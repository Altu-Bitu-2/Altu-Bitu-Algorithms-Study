from lib2to3.pgen2.token import NUMBER
import sys
import heapq as hq
input = sys.stdin.readline

def solution():
    n = int(input())
    
    # pypy3은 괜찮았지만, python3은 메모리 초과됨
    # table = [list(map(int, input().split())) for _ in range(n)]
    # max_heap = []
    
    # for i in range(n):
    #     hq.heappush(max_heap, (-table[-1][i], n-1, i))
    #     # 값, 행, 열
    
    # cnt = 0
    # while max_heap:
    #     cnt += 1
    #     val, x, y = hq.heappop(max_heap)
    #     if cnt == n: return -val
    #     if x: hq.heappush(max_heap, (-table[x-1][y], x-1, y))
    
    # 메모리를 줄이려면 저장하지 않고 바로 처리해주어야 함
    # 최소힙에 그때그때의 가장 큰 n개의 값을 저장
    
    min_heap = []
    for _ in range(n):
        numbers = map(int, input().split())
        if not min_heap:
            for num in numbers:
                hq.heappush(min_heap, num)
        else:
            for num in numbers:
                if min_heap[0] < num:
                    hq.heappop(min_heap)
                    hq.heappush(min_heap, num)
    
    return min_heap[0] # 최종 최소힙의 최소값이 n번째 큰 수 

if __name__ == "__main__":
    print(solution())