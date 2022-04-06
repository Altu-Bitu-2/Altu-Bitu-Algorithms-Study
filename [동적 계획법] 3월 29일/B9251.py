import sys
input = sys.stdin.readline

def solution():
    sequence1 = input().strip()
    sequence2 = input().strip()
    
    n = len(sequence1)
    m = len(sequence2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if sequence1[i - 1] == sequence2[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                
    print(dp[n][m])

if __name__ == "__main__":
    solution()