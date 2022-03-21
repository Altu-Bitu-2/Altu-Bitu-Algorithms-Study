import sys, math
input = sys.stdin.readline

def find_primes():
    primes = [False, False] + [True] * (MAX-1)
    
    for i in range(2, int(math.sqrt(MAX))+1):
        if primes[i]:
            for j in range(i*i, MAX+1, i):
                primes[j] = False
    return primes

def solution():
    
    primes = find_primes()
    while True:
        n = int(input())
        if not n: return
        
        for i in range(MAX+1):
            if primes[i] and primes[n-i]:
                print(f"{n} = {i} + {n-i}")
                break
            
if __name__ == "__main__":
    MAX = int(1e6)
    solution()