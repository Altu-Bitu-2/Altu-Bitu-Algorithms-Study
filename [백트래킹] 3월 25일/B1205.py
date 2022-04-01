import sys
input = sys.stdin.readline
        
def solution():
    n, t_score, p = map(int, input().split())
    
    # n이 0인 경우
    if n == 0:
        print(1)
        return
    
    scores = list(map(int, input().split()))
    
    # 범위 벗어나는 경우
    if n == p and scores[-1] >= t_score:
            print(-1)
            return

    # 범위 안인 경우
    for i in range(n):
        if scores[i] <= t_score:
            print(i + 1)
            return
    print(n+1)
    return

if __name__ == "__main__":
    solution()