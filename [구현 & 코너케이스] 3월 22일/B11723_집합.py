# 집합으로 접근 (틀린 접근)
# pypy3으로 제출하면 메모리초과가 남
# python3으로 제출하면 시간초과가 남

import sys
input = sys.stdin.readline

def solution():
    s = set()
    m = int(input())
    
    for _ in range(m):
        op = input().strip().split()
        
        if len(op) == 1:
            if op[0] == "all":
                s = {str(i) for i in range(1, 21)}
            else: # empty
                s.clear()
            continue

        op, x = op
        x = int(x)
        
        if op == "add":
            s.add(x)
        elif op == "remove":
            s.discard(x)
        elif op == "check":
            print(1 if x in s else 0)
        elif op == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)

if __name__ == "__main__":
    solution()