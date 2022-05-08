import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    score = [int(input()) for _ in range(n)]
    score = [0] + score
    
    if n == 1:
        print(score[1])
        return
    
    dp = score.copy()
    dp[2] += score[1]
    for i in range(3, n+1):
        dp[i] += max(score[i-1] + dp[i-3], dp[i-2])
    
    print(dp[n])

if __name__ == "__main__":
    solution()