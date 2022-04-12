import sys
import heapq as hq
input = sys.stdin.readline

def solution():
    
    # 시작시간 오름차순 정렬
    lectures.sort()
    
    # 한 강의실의 끝나는 시간 최소힙에 저장
    min_heap = []
    for s, t in lectures:
        hq.heappush(min_heap, t)
        
        # 시작 시간이 최소 끝나는 시간 이상이라면 같은 강의실 수업 가능
        if s >= min_heap[0]:
            hq.heappop(min_heap)
    
    return len(min_heap)
            
if __name__ == "__main__":
    n = int(input())
    
    lectures = []
    for _ in range(n):
        s, t = map(int, input().split())
        lectures.append((s, t))
    
    print(solution())