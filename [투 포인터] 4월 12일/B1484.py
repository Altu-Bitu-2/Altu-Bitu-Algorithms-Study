import sys
input = sys.stdin.readline

def two_pointers():
    left, right = 1, 2
    impossible = True
    while left < right and right <= MAX:
        tmp = right**2 - left**2
        if tmp == g: # 가능한 경우
            impossible = False
            print(right)
            left += 1
            right += 1
        elif tmp > g: left += 1
        else: right += 1
    
    if impossible: print(-1) # 불가능한 경우

if __name__ == "__main__":
    MAX = 50000 # 1 <= g <= 100,000이므로, right는 50000 이하여야 함
    g = int(input())
    two_pointers()
    