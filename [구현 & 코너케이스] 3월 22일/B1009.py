import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        last_digit = a % M
        if last_digit == 0:
            print(10)
        elif last_digit in [1, 5, 6]:
            print(last_digit)
        elif last_digit in [4, 9]:
            if b % 2:
                print(last_digit)
            else:
                print(last_digit * last_digit % M)
        else: # four
            r = b % 4
            if r == 0: r = 4
            ans = 1
            for i in range(r):
                ans *= last_digit
                ans %= M
            print(ans)

if __name__ == "__main__":
    M = 10
    solution()