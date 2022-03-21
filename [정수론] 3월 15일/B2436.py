import sys, math
input = sys.stdin.readline

def find_GCD(a, b):
    while(b):
        a, b = b,  a % b
    return a

def solution():
    gcd, lcm = map(int, input().split())
    tmp = lcm // gcd
        
    for i in range(int(math.sqrt(tmp)), 0, -1):
        if tmp % i == 0:
            if find_GCD(i, tmp // i) == 1:
                print(gcd * i, gcd * tmp // i)
                break
    
if __name__ == "__main__":
    solution()