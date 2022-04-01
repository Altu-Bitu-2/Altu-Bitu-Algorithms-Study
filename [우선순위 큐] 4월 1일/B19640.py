import sys
import heapq as hq
input = sys.stdin.readline

def solution(n, m, k):
    
    employees = []
    for i in range(n):
        d, h = map(int, input().split())
        employees.append((-d, -h, i % m, i))
        # 근무일수, 급한 정도, 줄의 번호, 인덱스
    
    heap = []
    
    # 우선순위 큐에 처음에 고려할 사람 수만큼 push
    if n < m:
        for i in range(n):
            hq.heappush(heap, employees[i])
    else:
        for i in range(m):
            hq.heappush(heap, employees[i])
    
    # 인덱스가 k인 경우를 찾을 때까지 
    # 우선순위 큐 pop 후 다음 선두가 될 사람 push
    cnt = 0
    while heap:
        d, h, _, i = hq.heappop(heap)
        if i == k: return cnt
        cnt += 1
        if n > i + m:
            hq.heappush(heap, employees[i + m])

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    print(solution(n, m, k))