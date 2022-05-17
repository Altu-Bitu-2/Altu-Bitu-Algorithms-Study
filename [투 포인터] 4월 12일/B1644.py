import sys, math
input = sys.stdin.readline

def find_primes(n):
    primes = [False, False] + [True] * (n-1)
    for i in range(2, int(math.sqrt(n))+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    primes = [i for i, v in enumerate(primes) if v]
    return primes

def accumulated_sum(primes):
    primes = [0] + primes
    for i in range(len(primes)):
        primes[i] += primes[i-1]
    return primes

def solution():
    primes = find_primes(n)
    primes = accumulated_sum(primes)
    
    cnt = 0
    visited = set()
    for prime in primes:
        if prime in visited:
            cnt += 1
        visited.add(n + prime)

    print(cnt)

if __name__ == "__main__":
    n = int(input())
    solution()