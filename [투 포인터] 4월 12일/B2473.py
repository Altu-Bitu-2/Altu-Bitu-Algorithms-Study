import sys
input = sys.stdin.readline

def solution():
    liquid.sort() # 정렬
    
    ans = 3 * int(1e9)
    left, mid = 0, 1
    
    while left < mid: # left 가 mid 보다 작을 때, left는 고정, mid와 right는 투 포인터
        mid = left + 1
        right = n - 1
        while mid < right:
            tmp_sum = liquid[left] + liquid[mid] + liquid[right]
            if abs(tmp_sum) < ans: # 합이 더 작을 때, 값 갱신
                ans = abs(tmp_sum)
                v1, v2, v3 = left, mid, right
            if tmp_sum < 0: # 합이 음수일 때 mid 오른쪽으로 이동
                mid += 1
            else: # 합이 양수 일 때 right 왼쪽으로 이동
                right -= 1
        left += 1 # left 오른쪽으로 이동
            
    print(liquid[v1], liquid[v2], liquid[v3])

if __name__ == "__main__":
    n = int(input())
    liquid = list(map(int, input().split()))
    solution()