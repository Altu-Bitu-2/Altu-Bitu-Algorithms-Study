import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    dp = [[0] * 10 for _ in range(n + 1)]
    
    for i in range(10):
        dp[1][i] = i + 1
        
    for i in range(2, n+1):
        for j in range(10):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 10007
    
    print(dp[n][9])
    
if __name__ == "__main__":
    solution()