import sys
input = sys.stdin.readline

def solution():
    n, p = map(int, input().split())
    cnt = 0
    stack = [[] for _ in range(n+1)]
    
    for _ in range(n):
        line, fret = map(int, input().split())
        while stack[line] and stack[line][-1] > fret:
                stack[line].pop()
                cnt += 1
        if  not stack[line] or stack[line][-1] < fret:
            stack[line].append(fret)
            cnt += 1
        
    print(cnt)
            
if __name__ == "__main__":
    solution()