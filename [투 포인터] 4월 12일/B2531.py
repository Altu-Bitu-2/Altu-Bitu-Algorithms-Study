import sys
from collections import deque
input = sys.stdin.readline

def solution():
    max_val = 0
    
    # 초밥 시작 위치에 대해 초밥 가짓수 개산
    for i in range(n): 
        choice = set()
        for j in range(i, i+k): # 연속되는 k개의 접시
            idx = j % n # 회전하는 벨트
            choice.add(dishes[idx])
        tmp = len(choice)
        if c not in choice: tmp += 1 # 쿠폰 포함
        
        max_val = max(tmp, max_val) # 초밥 가지수 최대값 계산

    print(max_val)
    
if __name__ == "__main__":
    n, d, k, c = map(int, input().split()) # 접시 수, 초밥 가지수, 연속 접시수, 쿠폰 번호
    dishes = [int(input()) for _ in range(n)]
    solution()