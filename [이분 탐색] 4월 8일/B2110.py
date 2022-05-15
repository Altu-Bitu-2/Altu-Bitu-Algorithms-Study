import sys
input = sys.stdin.readline

def count_routers(dist):
    cnt = 1
    now = houses[0]
    
    for i in range(1, n):
        if houses[i] - now >= dist:
            cnt += 1
            now = houses[i]
            
    return cnt

# 구하는 것: k개의 공유기를 설치가 되는, 최소 인접 거리의 최대값
def binary_search(left, right):
    while left <= right:
        mid = (left + right) // 2
        cnt = count_routers(mid)
        if cnt < k: right = mid - 1
        else: left = mid + 1
    
    return left - 1

def solution():
    houses.sort()
    return binary_search(1, houses[-1]-houses[0])

if __name__ == "__main__":
    n, k = map(int, input().split())
    houses = [int(input()) for _ in range(n)]
    
    print(solution())