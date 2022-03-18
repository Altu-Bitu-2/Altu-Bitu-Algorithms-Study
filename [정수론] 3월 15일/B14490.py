import sys
input = sys.stdin.readline

# 최대 공약수
def find_GCD(a, b):
    while(b):
        a, b = b,  a % b
    return a

def solution():
    n, m = map(int, input().split(':'))
    gcd = find_GCD(n, m)
    
    print(f"{n//gcd}:{m//gcd}")
    
if __name__ == "__main__":
    solution()