import sys
input = sys.stdin.readline
        
def solution():
    n, k = map(int, input().split())
    durability = list(map(int, input().split()))
    robot = [False] * (2 * n)

    up = 0
    down = n-1
    
    cnt = 0
    while(durability.count(0) < k): # 내구도 0인 칸 개수 k개 미만인 동안
        cnt += 1
        
        # 벨트 한 칸 회전
        up = (up - 1) % (2 * n)
        down = (up + (n - 1)) % (2 * n)

        # 로봇을 내림
        if robot[down]:
            robot[down] = False
        
        # 가장 먼저 벨트에 올라간 로봇부터 한 칸 이동
        for i in range(1, n):
            now = (down - i) % (2 * n)
            front = (down - i + 1) % (2 * n)
            if robot[now] and not robot[front] and durability[front] >= 1:
                robot[front] = True
                robot[now] = False
                durability[front] -= 1
        
        # 로봇을 내림
        if robot[down]:
            robot[down] = False
            
        # 로봇을 올림
        if durability[up] > 0:
            robot[up] = True
            durability[up] -= 1

    print(cnt)

if __name__ == "__main__":
    solution()