# 실시간 코딩 - 다시 풀기
import sys, math
input = sys.stdin.readline

def find_primes(n):
    primes = [False, False] + [True] * (n-1)
    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    primes = [i for i, v in enumerate(primes) if v and i <= n]
    return primes

def solution():
    primes = find_primes(n)
    primes.append(0)
    
    cnt = 0
    left, right = 0, 0
    subtotal = primes[left]
    while (left <= right and right < len(primes)-1):
        if subtotal == n:
            cnt += 1
            left += 1
            right += 1
        elif subtotal < n:
            right += 1
            subtotal += primes[right]
        else: # subtotal > n
            subtotal -= primes[left]
            left += 1

    return cnt

if __name__ == "__main__":
    n = int(input())
    print(solution())