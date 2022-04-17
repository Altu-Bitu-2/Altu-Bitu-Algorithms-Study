import sys
input = sys.stdin.readline

def solution():
    arr.sort() # 정렬
    
    ans = 0
    for i in range(n):
        tmp_arr = arr[:i] + arr[i+1:] # i번째 수를 제외한 배열에서
        
        left, right = 0, n-2
        while left < right:
            tmp_sum = tmp_arr[left] + tmp_arr[right]
            # 두 수의 합이 i 번째 수가 되는 경우가 있다면 1 증가
            if tmp_sum == arr[i]:
                ans += 1
                break
            elif tmp_sum < arr[i]: left += 1 # 두 수의 합이 더 작다면, 왼쪽 포인터 이동
            else: right -= 1 # 두 수의 합이 더 크다면, 오른쪽 포인터 이동
        
    return ans

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution())