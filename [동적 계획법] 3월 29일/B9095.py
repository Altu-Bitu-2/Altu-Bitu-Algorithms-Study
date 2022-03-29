import sys
input = sys.stdin.readline

def find_dp():
    dp = [0] * 11
    dp[1 : 4] = [1, 2, 4]
    for i in range(4, 11): dp[i] = sum(dp[i - 3 : i])
    return dp

def solution():
    n = int(input())
    print(dp[n])

if __name__ == "__main__":
    dp = find_dp()
    t = int(input())
    while t:
        t -= 1
        solution()