import sys
input = sys.stdin.readline

def calculate_time(height):
    remove, add = 0, 0 # 1번, 2번 작업 걸리는 시간
    inventory = b # 인벤토리 블록수
    for i in range(n):
        for j in range(m):
            difference = ground[i][j] - height 
            if difference >= 0: # 1번 작업, 작업 x
                remove += difference * 2
            else: # 2번 작업
                add -= difference
            inventory += difference # 인벤토리 갱신
    
    if inventory < 0: return INF # 인벤토리에 블록수 부족 시, 불가능
    return remove + add
                
def level_ground():
    min_height = 257
    max_height = -1
    
    for g in ground:
        min_height = min(min(g), min_height)
        max_height = max(max(g), max_height)
    
    # 모든 경우의 높이에 대해, 최소 시간 구하기
    time = INF
    height = min_height
    for h in range(max_height, min_height-1, -1):
        t = calculate_time(h)
        if t < time: time, height = t, h
    return time, height

if __name__ == "__main__":
    INF = int(1e9)
    n, m, b = map(int, input().split()) # 세로, 가로, 인벤토리 블록수
    ground = [list(map(int, input().split())) for _ in range(n)] # 땅의 높이
    print(" ".join(map(str, level_ground())))