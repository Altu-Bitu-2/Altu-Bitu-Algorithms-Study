import sys
import heapq as hq
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    
    mileage = []
    # 과목별 최소 할당해야하는 마일리지 계산
    for _ in range(n):
        p, l = map(int, input().split())
        others = list(map(lambda x : -int(x), input().split()))
    
        # 인원 미달
        if p < l: least = 1
        # 아니라면, l 번째 학생 마일리지 값 구하기
        else:
            hq.heapify(others)
            for _ in range(l):
                least = -hq.heappop(others)
        
        mileage.append(least)

    # 수강할 수 있는 최대 과목 수 구하기
    hq.heapify(mileage)    
    cnt = 0
    while mileage:
        m -= hq.heappop(mileage)
        if m < 0: break
        cnt += 1
    
    print(cnt)
    
if __name__ == "__main__":
    solution()