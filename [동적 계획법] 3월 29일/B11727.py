import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    dp = [0, 1, 3, 5] + [0] * (n - 3)

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2
    
    print(dp[n] % 10007)

if __name__ == "__main__":
    solution()