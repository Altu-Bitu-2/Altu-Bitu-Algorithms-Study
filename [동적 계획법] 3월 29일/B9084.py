import sys
input = sys.stdin.readline

def solution():
        n = int(input())
        coins = list(map(int, input().split()))
        amount = int(input())
        dp = [0] * (max(amount, coins[-1]) + 1)
        
        for i in range(n):
            dp[coins[i]] += 1
            for j in range(coins[i] + 1, amount + 1):
                dp[j] += dp[j - coins[i]]

        print(dp[amount])

if __name__ == "__main__":
    t = int(input())
    while(t):
        t -= 1
        solution()