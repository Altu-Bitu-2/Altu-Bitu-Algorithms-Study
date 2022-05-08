import sys
from collections import deque
input = sys.stdin.readline

# bfs로 연결된 뿌요들 찾기
def find_group(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    brust = [] # 터질 뿌요
    q = deque()
    q.append((x, y))
    count = 1 # 연결된 같은 색 뿌요들 개수
    
    while q:
        x, y = q.pop()
        brust.append((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > 11 or ny > 5: continue
            if field[nx][ny] == ".": continue
            if (nx, ny) in brust: continue
            if field[nx][ny] == field[x][y]:
                q.append((nx, ny))
                count += 1
    
    # 연결된 뿌요들 터지기
    if count >= 4:
        for x, y in brust:
            field[x][y] = "."
        
        return True # 연쇄가 일어나는 그룹 있음
    
    return False # 연쇄가 일어나는 그룹 없음
    

def chain_reaction():
    stop = True # 연쇄가 일어나는 그룹 있다면 False
    
    # 연쇄 하나에 뿌요 그룹 찾기
    for i in range(12):
        for j in range(6):
            flag = find_group(i, j)
            if flag: stop = False
    
    if stop: return False # 끝
    
    # 터진 뿌요들 내려가기
    for j in range(6):
        column = []
        for i in range(11, -1, -1):
            if field[i][j] != '.':
                column.append(field[i][j])

        for i in range(11, 11 - len(column), -1):
            field[i][j] = column[11 - i]

        for i in range(11 - len(column), -1, -1):
            field[i][j] = "."
            
    return True # 끝 아님
            
def count_chain_reactions():
    
    count = 0
    while chain_reaction():
        count += 1
    return count

if __name__ == "__main__":
    field = [list(input().rstrip()) for _ in range(12)] # 필드 정보
    print(count_chain_reactions())