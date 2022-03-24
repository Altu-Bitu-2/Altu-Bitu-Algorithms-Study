# 비트마스크로 접근
# 어려웠던 점:
# pypy3으로 제출하면 메모리 초과가 남
# python3으로 제출해서 해결

import sys
input = sys.stdin.readline

def solution():
    s = 0
    m = int(input())
    
    for _ in range(m):
        op = input().strip().split()
        
        if len(op) == 1: # 단어 수 1개인 연산들
            if op[0] == "all":
                s = ~(1 << 21)
            else: # empty
                s = 0
            continue
        
        # 단어 수 2개인 연산들
        op, x = op
        x = int(x)
        
        if op == "add":
            s |= 1 << x
        elif op == "remove":
            s &= ~(1 << x)
        elif op == "check":
            print(1 & (s >> x))
        elif op == "toggle":
            s ^= (1 << x)

if __name__ == "__main__":
    solution()