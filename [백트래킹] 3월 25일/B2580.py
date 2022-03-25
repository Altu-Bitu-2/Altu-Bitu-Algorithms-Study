import sys
input = sys.stdin.readline
    
def check(x, y):
    numbers = {i for i in range(1, 10)}
    
    for i in range(9):
        numbers.discard(stoku[x][i]) # 가로줄
        numbers.discard(stoku[i][y]) # 세로줄
        # 3x3 정사각형
        s, t = (x//3) * 3 + (i//3), (y//3) * 3 + (i % 3)
        numbers.discard(stoku[s][t]) 
        
    for i in range(x//3 * 3, (x//3 + 1) * 3):
        for j in range(y//3 * 3, (y//3 + 1) * 3):
            if stoku[i][j] in numbers:
                numbers.discard(stoku[i][j])
                
    return numbers

def backtracking(cnt):
    global found
    if found: return # 하나만 출력
    
    # 최종 모습 출력
    if cnt == len(blank):
        [print(" ".join(map(str, row))) for row in stoku]
        found = True
        return
    
    # 가능한 숫자 확인
    x, y = blank[cnt]
    cases = check(x, y)
    
    # 각 숫자에 대해 백트래킹
    for case in cases:
        stoku[x][y] = case
        backtracking(cnt+1)
        stoku[x][y] = 0
    
if __name__ == "__main__":
    found = False
    stoku = [list(map(int, input().split())) for _ in range(9)]
    blank = [(i, j) for i in range(9) for j in range(9) if stoku[i][j] == 0]
    backtracking(0)