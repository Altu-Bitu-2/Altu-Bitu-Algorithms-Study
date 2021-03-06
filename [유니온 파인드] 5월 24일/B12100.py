import sys
input = sys.stdin.readline

"""
 [2048 (Easy)]

 - 상, 하, 좌, 우로 이동하는 경우에 대해 최대 5번 이동시키는 모든 경우를 구한 후, 가장 큰 블록 찾는 문제 - 백트래킹
 - 움직이는 함수는 하나만 짜고, 보드를 돌려가면서 상, 하, 좌, 우 모든 방향의 움직임을 만듦

 - 상 <-> 하: 행 순서를 뒤집어서 해결
 - 상/하 <-> 좌/우: Transpose Matrix 활용

 - ex. 2 2 1 를 상, 하, 좌, 우로 이동하는 경우 구하는 법
       2 2 2
       4 4 4
  -상: 원래 배열에서 상으로 움직이는 함수 실행
       2 2 1    4 4 1
       2 2 2 -> 4 4 2
       4 4 4    0 0 4
  -하: 원래 배열의 행 순서를 뒤집은 후, 상으로 움직이는 함수 실행
       2 2 1    4 4 4    4 4 4
       2 2 2 -> 2 2 2 -> 4 4 2
       4 4 4    2 2 1    0 0 1
  -좌: 원래 배열의 전치 행렬을 구한 후, 상으로 움직이는 함수 실행
       2 2 1    2 2 4    4 4 8
       2 2 2 -> 2 2 4 -> 1 2 4
       4 4 4    1 2 4    0 0 0
  -우: 원래 배열의 전치 행렬에서 행 순서를 뒤집은 후, 상으로 움직이는 함수 실행
       2 2 1    1 2 4    1 4 8
       2 2 2 -> 2 2 4 -> 4 2 4
       4 4 4    2 2 4    0 0 0

 - zip(): 두개 이상의 iterable한 객체를 인자로 받아서, 순서대로 하나씩 묶어서 반환한다.
    ex) zip([1, 2, 3], ['a', 'b', 'c']) -> [1, 'a'], [2, 'b'], [3, 'c']
    따라서 zip의 인자로 각 행을 넣어주면, 행과 열이 바뀐 Transpose matrix가 나오게 된다.
"""

def up(board): # 블록을 위로 움직이는 것을 시뮬레이션하는 함수
    """
    위로 움직이는 함수
    한 열씩 검사하면서 위의 행부터 2개씩 같은 거 있다면 합치기
    이때 블록 없는 부분은 넘어가고, 블록이 존재했던 값을 저장해서 비교하는 것이 중요!
    """
    temp = [[0]*n for _ in range(n)] # 위로 움직인 결과를 저장할 리스트
    for c in range(n): # 한 열씩 검사
        idx = 0 # 위로 움직인 결과 리스트의 인덱스
        prev = 0 # 이전 값 저장할 변수 0으로 초기화
        for r in range(n): # 위의 행부터 검사
            if not board[r][c]: # 만약 블록이 없다면
                continue # 넘어가기
            if board[r][c] == prev: # 이전에 존재했던 값과 같다면
                temp[idx-1][c] *= 2 # 이전 블록 값 2배하기
                prev = 0 # 합쳐진 블록이므로 prev 0으로 초기화
            else: # 이전에 존재했던 값과 다르다면
                temp[idx][c] = board[r][c] # 현재 인덱스에 결과 저장
                prev = board[r][c] # 현재 블록 값 prev 변수에 저장
                idx += 1 # 인덱스 1 증가

    return temp # 위로 움직인 결과 리스트 반환

def backtracking(cnt, board): # 이동한 횟수 카운드 변수 cnt, 게임판 상태를 매개변수로 받는 백트래킹 함수
    global ans # 백트래킹으로 값을 갱신해줄 전역변수 ans 선언
    if cnt == 5: # 5번 이동한 경우
        for line in board: # 각 행에서
            ans = max(ans, max(line)) # 가장 큰 값 찾기
        return # 반환

    # Transpose matrix 구하기 (상 -> 좌)
    board_t = list(zip(*board)) # zip, * 을 이용해 transpose matrix 구하기

    # 상
    backtracking(cnt+1, up(board)) # 1 증가된 이동횟수 변수, 상 방향으로 움직인 게임판 리스트를 인자로 넘기기
    # 하
    backtracking(cnt+1, up(board[::-1])) # 1 증가된 이동횟수 변수, 행 기준으로 역방향으로 바꾼 게임판 리스트를 상방향으로 움직인 결과 리스트를 인자로 넘기기
    # 좌
    backtracking(cnt+1, up(board_t)) # 1 증가된 이동횟수 변수, 열과 행이 바뀐 게임판 리스트를 상방향으로 움직인 결과 리스트를 인자로 넘기기
    # 우
    backtracking(cnt+1, up(board_t[::-1])) # 1 증가된 이동횟수 변수, 열과 행이 바꾸고 행 기준으로 역방향으로 바꾼 리스트를 상방향으로 움직인 결과 리스트를 인자로 넘기기

    return # 반환

# 입력
n = int(input()) # 보드의 크기
board = [list(map(int, input().split())) for _ in range(n)] # 게임판의 초기 상태 2차원 리스트로 저장

ans = 0 # 최대 5번 이동시켜서 얻을 수 있는 가장 큰 볼록 저장할 변수 0으로 초기화
backtracking(0, board) # 상, 하, 좌, 우로 이동하는 것에 대해 백트래킹으로 완전 탐색

# 출력
print(ans) # 최대 5번 이동시켜서 얻을 수 있는 가장 큰 볼록 출력