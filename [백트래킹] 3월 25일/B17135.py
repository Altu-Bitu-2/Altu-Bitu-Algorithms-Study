import sys
input = sys.stdin.readline

def available_size(x, y):
    for size in range(5, 0, -1):
        if x + size > 9 or y + size > 9: continue
        
        flag = False
        for i in range(x, x + size):
            if flag: break
            for j in range(y, y + size):
                if paper[i][j] == 0:
                    flag = True
                    break
        if not flag: return True, size
    
    return False, 0

def operate(x, y, size):
    for i in range(size):
        for j in range(size):
            paper[x+i][y+j] = 1 - paper[x+i][y+j]
                 
def backtracking(idx, cnt):
    global ans, colored_papers
    
    if idx == 100:
        if cnt < ans: ans = cnt
        return
    
    x, y = idx // 10, idx % 10
    
    # 0 적힌 칸
    if paper[x][y] == 0: 
        backtracking(idx+1, cnt)
        return
    
    # 1 적힌 칸
    for size in range(5, 0, -1):
        
        if colored_papers[size] == 0: continue # 종이 없음
        if x + size > 10 or y + size > 10: continue # 범위 벗어남
        
        # 맞는 사이즈 찾기
        flag = False
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] == 0:
                    flag = True
                    break
            if flag: break
         
        # 사이즈 맞음
        if not flag:        
            operate(x, y, size) # 붙이기
            colored_papers[size] -= 1
            backtracking(idx+1, cnt+1)
            colored_papers[size] += 1
            operate(x, y, size) # 떼어내기

if __name__ == "__main__":
    M = 26
    ans = M
    paper = [list(map(int, input().split())) for _ in range(10)]
    colored_papers = [5] * 6
    backtracking(0, 0)
    print(ans if ans != M else -1)