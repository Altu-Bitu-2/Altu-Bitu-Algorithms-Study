import sys
from itertools import combinations
input = sys.stdin.readline
            
def solution():
    _, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    ans = 0
    for nums in combinations(numbers, 3):
        tmp = sum(nums)
        if tmp <= m:
            if ans < tmp: ans = tmp
            
    print(ans)
    
if __name__ == "__main__":
    INF = int(1e9)
    solution()