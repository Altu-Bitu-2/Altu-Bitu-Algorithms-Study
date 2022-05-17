import sys
input = sys.stdin.readline

def accumulative_sum():
    for i in range(1, n):
        arr[i] += arr[i-1]
            
def solution(i, j):
    if i == 0: return arr[j]
    return arr[j] - arr[i-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    accumulative_sum()
    
    for _ in range(m):
        i, j = map(int, input().split())
        print(solution(i-1, j-1))