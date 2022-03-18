import sys, math
input = sys.stdin.readline

def is_prime():
    primes = [-1, -1] + [0] * (MAX-1)
    for i in range(2, int(math.sqrt(MAX))):
        if primes[i] == 0:
            for j in range(i*i, MAX+1, i):
                primes[j] = i
    return primes

def add_primes(num):
    if num == 1:
        return
    while primes[num]:
        factorized[primes[num]] += 1
        num //= primes[num]    
    factorized[num] += 1
    
def sub_primes(num):
    if num == 1:
        return
    while primes[num]:
        factorized[primes[num]] -= 1
        num //= primes[num]
    factorized[num] -= 1

def solution():
    n = int(input())
    formula = list(input().strip().split())

    if '0' in formula:
        print("mint chocolate")
        return
    
    add_primes(abs(int(formula[0])))
    for i in range(2, 2 * n - 1, 2):
        num = abs(int(formula[i]))
        if formula[i-1] == '*': 
            add_primes(num)
        elif formula[i-1] == '/': 
            sub_primes(num)
       
    for cnt in factorized:
        if cnt < 0:
            print("toothpaste")
            return
        
    print("mint chocolate")
        
if __name__ == "__main__":
    MAX = int(1e5)
    factorized = [0] * (MAX + 1)
    primes = is_prime()
    solution()