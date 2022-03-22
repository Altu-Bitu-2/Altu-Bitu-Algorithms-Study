import sys
input = sys.stdin.readline

def count_square(start_i, start_j):
    ans = INF
    for t in range(2):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if target_board[t][i][j] != input_board[start_i + i][start_j + j]:
                    cnt += 1
        if cnt < ans: ans = cnt
    return ans
    
def make_targets():
    board = [[] for _ in range(2)]
    for t in range(2):
        for i in range(8):
            tmp = []
            for j in range(8):
                if (i+j+t) % 2:
                    tmp.append('W')
                else:
                    tmp.append('B')
            board[t].append(tmp)
    
    return board
    
def solution():
    n, m = map(int, input().split())

    [input_board.append(list(input().strip())) for _ in range(n)]
    
    ans = INF 

    for i in range(n-7):
        for j in range(m-7):
            cnt = count_square(i, j)
            if cnt < ans: ans = cnt
    
    if ans == INF:
        ans = 0
        
    print(ans)
            
                
if __name__ == "__main__":
    INF = int(1e9)
    input_board=[]
    target_board = make_targets()

    solution()