import sys
import heapq as hq
input = sys.stdin.readline

def solution():
    min_heap = []
    max_heap = []
    saved_data = [False] * int(1e6)
    
    k = int(input())
    
    for i in range(k):
        op, n = input().split()
        n = int(n)
        
        # 정수 n을 Q에 삽입 연산
        if op == "I":
            hq.heappush(min_heap, (n, i))
            hq.heappush(max_heap, (-n, i))
            saved_data[i] = True
        
        else:
            # Q에서 최대값 삭제 연산
            if n == 1:
                while max_heap and not saved_data[max_heap[0][1]]:
                    hq.heappop(max_heap)
                if max_heap:
                    saved_data[max_heap[0][1]] = False
                    hq.heappop(max_heap)
                    
            # Q에서 최소값 삭제 연산
            else: 
                while min_heap and not saved_data[min_heap[0][1]]:
                    hq.heappop(min_heap)
                if min_heap:
                    saved_data[min_heap[0][1]] = False
                    hq.heappop(min_heap)

    # 출력
    while max_heap and not saved_data[max_heap[0][1]]:
        hq.heappop(max_heap)
    while min_heap and not saved_data[min_heap[0][1]]:
        hq.heappop(min_heap)
    
    if max_heap: print(-max_heap[0][0], min_heap[0][0])
    else: print("EMPTY")

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        solution()