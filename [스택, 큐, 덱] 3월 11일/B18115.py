import sys
from collections import deque
input = sys.stdin.readline

def solution():
    
    n = int(input())
    tricks = list(map(int, input().split()))
    tricks.reverse()
    
    d = deque()

    for i in range(n):
        if tricks[i] == 1:
            d.append(i+1)
        elif tricks[i] == 2:
            d.insert(i-1, i+1)
        else:
            d.appendleft(i+1)
    
    while d:
        print(d.pop(), end=' ')
    print()
    
if __name__ == "__main__":
    solution()