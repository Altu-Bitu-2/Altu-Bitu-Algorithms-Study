from itertools import permutations # 순열 계산
from collections import deque # bfs를 위한 큐

SIZE = 4 # 현재 카드가 놓인 상태를 나타내는 2차원 배열의 행, 열 크기
CNT = 6 # 카드 종류 최대값

dr = [-1, 1, 0, 0] # 상, 하, 좌, 우 한 칸 이동에 대한 행 변화값 저장 리스트
dc = [0, 0, -1, 1] # 상, 하, 좌, 우 한 칸 이동에 대한 열 변화값 저장 리스트

"""
 [카드 짝 맞추기]

 아이디어
 1. 범위가 크지 않음
 2. 존재하는 모든 카드의 종류는 6개, 카드 2장이 한 쌍을 이룬다.
 3. 뒤집을 카드 순서를 정하는 모든 경우의 수는 6!(카드 순서) * 2^6(2개의 카드 중 어떤 카드를 먼저 뒤집을지) -> 브루트포스 가능
 4. 이번에 목표로 하는 카드에 대해 현재 커서에서 목표 카드까지 가는 최단 경로를 구하며 이동 횟수 전부 구하고 최솟값 갱신

 구현
 1. 존재하는 모든 카드의 위치를 저장하며 카드의 개수 세기 (find_cards)
 2. 가능한 모든 카드의 순서(permutations)와 각 카드를 뒤집을 순서(bitmask)를 결정
    ex) seq = {3, 1, 2}, bit = 011 일 때
        3번, 1번, 2번 카드의 순서로 뒤집는다.
        3번 카드는 1번째 카드부터, 1번 카드는 0번째 카드부터, 2번 카드는 1번째 카드부터 뒤집는다.
        bit의 011이 앞에서부터 각각 1, 2, 3번 카드와 대응함
 3. 현재 카드 순서와 각 카드를 뒤집는 순서에 대한 커서 이동 횟수 계산 (match_card)
    현재 커서 위치와 목표 카드 위치에 대해 bfs 함수 실행
    컨트롤 입력을 고려해야 하기 때문에 4방향에 대한 방향 이동에 추가로 컨트롤 입력도 처리한다.(ctrl)
 4. 매 조합에 따라 board가 갱신되므로 board를 복사한 tmp 사용
 공식 풀이 : https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
"""

# 컨트롤로 이동하는 좌표를 리턴하는 함수
def ctrl(row, col, dir, tmp): # 현재 좌표, 방향키 방향, 현재 보드 상태를 매개변수로 받아 이동한 좌표 반환
    while True: # 무한 루프
        row += dr[dir] # 다음 위치 행
        col += dc[dir] # 다음 위치 열
        # 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동
        if not (0 <= row < SIZE) or not(0 <= col < SIZE): # 보드 범위 안이 아니라면
            return (row - dr[dir], col - dc[dir]) # 계산하기 전 좌표 반환
        # 누른 키 방향에 있는 가장 가까운 카드
        if tmp[row][col]: # 만약 카드가 존재한다면
            return (row, col) # 해당 좌표 반환

# 현재 커서에서 목표 카드로 이동하는 가장 적은 비용을 리턴하는 함수
def bfs(r1, c1, r2, c2, tmp):
    # 첫 시작 위치에 카드가 있는 경우
    if r1 == r2 and c1 == c2: # 좌표 일치
        return 1 # 바로 [Enter]

    visited = [[0]*SIZE for _ in range(SIZE)] # 방문할 때까지 조작한 횟수를 저장하고 방문 여부를 체크할 2차원 리스트
    que = deque() # bfs를 위한 큐
    # 반드시 엔터를 누르게 될 것. 엔터를 미리 눌렀다 가정하고 1로 표시
    visited[r1][c1] = 1 # 처음 위치 1로 표시
    que.append((r1, c1)) # 큐에 처음 칸 좌표 저장

    while que: # 큐가 빌 때까지
        row, col = que.popleft() # 큐에서 현재 탐색 좌표 pop
        dist = visited[row][col] # 현재 위치까지의 조작한 횟수 dist 변수에 저장
        
        # 컨트롤 입력 이동
        for i in range(4): # 상, 하, 좌, 우 각 방향에 대해
            nr, nc = ctrl(row, col, i, tmp) # 누른 키 방향에 있는 가장 가까운 카드로 한번에 이동한 좌표 계산
            if not visited[nr][nc]: # 아작 방문하지 않음
                visited[nr][nc] = dist + 1 # 현재 위치까지 거리에 1을 추가하여 저장
                # 목표 카드에 도달했다면
                if nr == r2 and nc == c2: # 목표 카드와 좌표 같다면, 목표 카드 도달
                    return dist + 1 # 해당 좌표까지의 조작한 횟수 반환
                que.append((nr, nc)) # 목표 카드와 좌표 같지 않다면, 큐에 이동한 좌표 저장

        # 방향키 입력 이동
        for i in range(4): # 상, 하, 좌, 우 각 방향에 대해
            nr, nc = row + dr[i], col + dc[i] # 1칸 이동한 좌표 계산
            if (0 <= nr < SIZE) and (0 <= nc < SIZE) and not visited[nr][nc]: # 범위 안에 있고, 방문하지 않은 칸이라면
                # 목표 카드에 도달했다면
                if nr == r2 and nc == c2: # 목표 카드와 좌표 같다면, 목표 카드 도달
                    return dist + 1 # 해당 좌표까지 조작한 횟수 반환
                visited[nr][nc] = dist + 1 # 목표카드와 좌표 같지 않다면, 조작한 횟수 저장
                que.append((nr, nc)) # 큐에 이동한 좌표 저장

    # 목표 카드에 도달하지 못함 (실제로는 일어나지 않는 일)
    return -1 # 도달하지 않을 경우 -1 반환

# 조합에 대해 카드를 매칭하는 함수
def match_card(bit, num, r, c, seq, cards, board, answer): # 두 개의 카드 중 먼저 뒤집는 순서 bit, 카드 종류 최대값 card_cnt, 카드 종류 순서 seq 등을 매개변수로 전달받아, 모든 카드를 제거하기 위한 키 조작 쵯수의 최소값 반환
    tmp = [] # 현재 board 상태를 저장할 임시 배열
    for line in board: # 각 행에 대해
        tmp.append(line[:]) # tmp 깊은 복사한 리스트 추가

    ans = 0 # 조작 횟수 변수 0으로 초기화
    for i in range(num): # seq의 카드 차례대로
        curr = seq[i]   # 이번에 매칭할 캐릭터

        if not cards[curr]: # 만약 card가 존재하지 않다면
            continue # 다음 카드 선택

        now = 0 # 해당 캐릭터의 0번째 카드부터 선택한다고 가정
        
        # 만약 해당 위치의 비트가 1을 표시했다면 1번째 카드부터 선택
        if bit & (1 << i): # i 번째 비트가 1이면
            now = 1 # 처음 뒤집는 카드 0번째 카드가 아닌 1번째 카드 선택

        for _ in range(2): # 두 개의 카드에 대해
            nr, nc = cards[curr][now]    # 이번에 매칭할 카드 위치
            ans += bfs(r, c, nr, nc, tmp)   # 현재 커서에서 목표 카드까지 이동하는 비용 # 조작하는 횟수

            # 기존 최솟값보다 큰 경우 -> 더 이상의 탐색 불필요 # 최소값을 찾기 때문에
            if ans >= answer: # 기존의 최소값보다 큰 경우
                return answer # 정답 반환

            # 카드 삭제 + 커서 이동
            tmp[nr][nc] = 0 # 카드 삭제 # 0으로 빈칸 표시
            r, c = nr, nc # 커서 이동 # 삭제한 카드 위치로 커서 이동
            now = 1 - now   # 다음에 매칭할 카드 인덱스 # 0이었다면 1, 1이었다면 0
    
    return ans # 해당 경우에 대한 모든 카드를 제거하기 위한 키 조작 쵯수의 최소값 반환

# 존재하는 모든 카드의 위치를 리턴하는 함수
def find_cards(board): # 현재 카드가 놓인 상태를 나타내는 2차원 배열 board를 받아 
    cards_pos = [list() for _ in range(CNT + 1)]   # 최대 카드 수 # 각 카드의 위치를 저장할 리스트
    cnt = 0 # 카드의 최대값 변수
    for i in range(SIZE): # 각 행에 대해
        for j in range(SIZE): # 각 열에 대해
            if not board[i][j]: # 만약 빈 칸이라면
                continue # 다음 칸으로 넘어가기
            cnt = max(cnt, board[i][j]) # 최대값으로 갱신
            cards_pos[board[i][j]].append((i, j)) # 각 카드의 위치 리스트에 저장
    return cards_pos, cnt # 각 카드의 위치 저장한 리스트, 카드의 최대값 반환

def solution(board, r, c): # 현재 카드가 놓인 상태를 나타내는 2차원 배열 board, 커서의 처음 위치 r,c 가 매개변수로 주어지면 모든 카드를 제거하기 위한 키 조작 횟수의 최솟값 반환하는 함수
    answer = 10**9 # 최소값을 구하기 위해 가능한 경우의 최대값으로 초기화
    cards, card_cnt = find_cards(board)    # 존재하는 모든 카드의 위치 # 각 카드의 위치 리스트, 카드 최대값
    
    # 가능한 모든 순서에 대해
    for seq in permutations(range(1, card_cnt+1), card_cnt): # 카드 종류(1, 2, ...,카드 종류 최대값)를 중복없이 나열하는 모든 경우에 대하여 
        for bit in range(1 << card_cnt): # 0, ..., 2^(카드 종류 최대값) - 1 -> 두 개의 카드 중 먼저 뒤집는 모든 경우(0, 1)에 대해
            answer = match_card(bit, card_cnt, r, c, seq, cards, board, answer) # 두 개의 카드 중 먼저 뒤집는 순서 bit, 카드 종류 최대값 card_cnt, 카드 종류 순서 seq 등을 매개변수로 전달하여, 모든 카드를 제거하기 위한 키 조작 쵯수의 최소값 반환받기
    return answer # 정답 반환

if __name__ == "__main__": # 현재 스크립트 파일이 메인 프로그램이라면
    board = [[1, 0, 0, 3],
             [2, 0, 0, 0],
             [0, 0, 0, 2],
             [3, 0, 1, 0]] # 현재 카드가 놓인 상태를 나타내는 2차원 배열 예시
    print(solution(board, 1, 0)) # 모든 카드를 제거하기 위한 키 조작 횟수 최소값 출력