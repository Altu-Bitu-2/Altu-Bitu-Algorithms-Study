import sys, math
input = sys.stdin.readline
            
def solution():
    n = int(input())
    dp = [INF] * (n+1)
    
    for i in range(1, int(math.sqrt(n))+1):
        dp[i*i] = 1
    
    for i in range(1, n+1):
        if dp[i] != 1:
            for j in range(1, int(math.sqrt(i)+1)):
                dp[i] = min(dp[i], dp[i-j*j]+1)
    
    print(dp[n])
    
if __name__ == "__main__":
    INF = int(1e9)
    solution()