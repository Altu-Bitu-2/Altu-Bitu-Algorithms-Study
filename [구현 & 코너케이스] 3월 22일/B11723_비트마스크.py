# 비트마스크로 접근
# pypy3으로 제출하면 메모리 초과가 남
# python3으로 제출해서 해결

import sys
input = sys.stdin.readline

def solution():
    s = 0
    m = int(input())
    
    for _ in range(m):
        op = input().strip().split()
        
        if len(op) == 1:
            if op[0] == "all":
                s = ~(1 << 21)
            else:
                s = 0
            continue
        
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