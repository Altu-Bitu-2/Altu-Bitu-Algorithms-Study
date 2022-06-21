"""
[기둥과 보 설치]

들어오는 입력에 대해 설치 또는 삭제 이후에도 기본 조건에 만족하는지 확인

[기본 조건]
1. 기둥
    a. 바닥 위
    b. 보의 한 쪽 끝
    c. 다른 기둥 위
2. 보
    a. 한쪽 끝이 기둥 위
    b. 양쪽 끝이 보와 연결

- 설치: 설치하려는 좌표가 조건을 만족하는지 확인
- 삭제: 해당 기둥/보를 삭제했을 시 영향을 받는 인접한 기둥/보가 여전히 조건을 만족하고 있는지 확인
"""

board = [] # 구조물 설치 현황 저장할 3차원 리스트

# 현재 상태가 조건에 만족하는지 (x, y) 중심으로 확인 
def validate(x, y, a, n): # 좌표, 구조물 종류, 벽면 크기를 매개변수로 받아 구조물이 설치 가능한지를 boolean 값으로 반환하는 함수
    # 기둥
    if a == 0: # 기둥을 설치하려 할 때,
        # 바닥 위
        if y == 0: # 바닥 바로 위 (x, 0) 에 설치한다면
            return True # 기둥 설치 가능
        # 보의 왼쪽/오른쪽 끝
        if board[x][y][1] or (x > 0 and board[x-1][y][1]): # 오른쪽 보 (x, y) 또는 왼쪽 보 (x-1, y) 있다면
            return True # 기둥 설치 가능
        # 기둥 위
        if y > 0 and board[x][y-1][0]: # 아래 기둥 (x, y-1) 있다면
            return True # 기둥 설치 가능
        
    # 보
    else: # 보를 설치하려 할 때,
        # 왼쪽 끝이 기둥 위
        if y > 0 and board[x][y-1][0]: # 왼쪽 기둥 (x, y-1) 있다면
            return True # 보 설치 가능
        # 오른쪽 끝이 기둥 위
        if x < n and y > 0 and board[x+1][y-1][0]: # 오른쪽 기둥 (x+1, y-1) 있다면
            return True # 보 설치 가능
        # 양쪽 끝이 보와 연결
        if 0 < x < n-1 and board[x-1][y][1] and board[x+1][y][1]: # 왼쪽 보 (x-1, y) 그리고 오른쪽 보 (x+1, y) 있다면
            return True # 보 설치 가능
        
    return False # 모든 설치 가능한 경우가 안된다면, 설치 불가능

# (x, y)에 있는 구조물을 삭제할 수 있는지 확인
def check_removable(x, y, n): # 좌표, 벽면 크기를 매개변수로 받아 구조물이 삭제 가능한지를 boolean 값으로 반환하는 함수
    # 기둥이 삭제된 경우, 해당 기둥 위에 보가 있었을 수 있으므로 (조건 2-b) 대각선도 확인이 필요
    for dx in (-1, 0, 1): # 이전 행, 현재 행, 다음 행 (왼쪽, 현재, 오른쪽)
        for dy in (-1, 0, 1): # 이전 열, 현재 열, 다음 열 (아래쪽, 현재, 윗쪽)
            nx, ny = x+dx, y+dy # 체크할 좌표 계산
            if not (0<= nx <= n and 0 <= ny <= n): # 범위 내에 없다면
                continue # 다음 좌표로 넘어가기
            for j in range(2): # 두 가지 구조물에 대해
                if board[nx][ny][j] and not validate(nx, ny, j, n): # 구조물이 있고, 설치 가능하지 않다면
                    return False # 삭제 할 수 없음

    return True # 모든 주변 구조물에 대해 체크한 결과 모두 설치 가능하다면 삭제 가능함

def solution(n, build_frame): # 벽면 크기 n, 기둥과 보를 설치하거나 삭제하는 작업 순서대로 담긴 build_frame 매개변수
    global board
    
    board = [[[False] * 2 for _ in range(n+1)] for _ in range(n+1)] # 현재 설치 현황 (0: 기둥, 1: 보 => [기둥, 보])
    answer = [] # 모든 명령어를 수행한 후 구조물 상태 담을 리스트

    for x, y, a, b in build_frame: # 기둥, 보 설치 또는 삭제할 교차점 좌표의 가로 좌표, 세로 좌표, 설치 또는 삭제할 구조물의 종류 (0: 기둥, 1: 보), 구조물을 설치할지, 삭제할 지 (0: 삭제, 1: 설치)
        # 삭제
        if b == 0: # b가 0이면 삭제
            board[x][y][a] = False # 해당 좌표의 구조물 일단 삭제
            # 삭제할 수 없으면
            if not check_removable(x, y, n): # 삭제 가능하다면 True, 삭제 불가능하다면 False
                board[x][y][a] = True # 삭제 불가능하다면, 삭제한 구조물 다시 설치
        # 설치
        else: # b가 1이면 설치
            # 설치 가능한 경우
            if validate(x, y, a, n): # 설치 가능하다면 True, 설치 불가능하다면 False
                board[x][y][a] = True # 설치 가능한 경우, 설치하기
                
    for i in range(n+1): # 각 행에 대해
        for j in range(n+1): # 각 열에 대해
            for k in range(2): # 각 구조물에 대해
                if board[i][j][k]: # 설치되어있다면
                    answer.append([i, j, k]) # 반환할 리스트에 추가
    return answer # 모든 명령어를 수행한 후 구조물 상태 리턴

if __name__ == "__main__":
    n = 5 # 벽면 크기 예시
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]] # 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 build_frame 예시
    print(solution(n, build_frame)) # 결과 리스트 출력