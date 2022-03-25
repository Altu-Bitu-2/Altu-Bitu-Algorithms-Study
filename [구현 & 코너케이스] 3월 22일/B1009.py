import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        last_digit = a % M # 마지막 자리수
        
        # 거듭제곱한 결과값의 마지막 자리수가 1, 2, 4의 주기로 반복됨
        if last_digit == 0: # 0일 때
            print(10)
        elif last_digit in [1, 5, 6]: # 항상 동일한 마지막 자리수
            print(last_digit)
        elif last_digit in [4, 9]: # 2가지 마지막 자리수
            if b % 2:
                print(last_digit)
            else:
                print(last_digit * last_digit % M)
        else: # 4가지 마지막 자리수
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