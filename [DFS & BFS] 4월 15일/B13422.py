import sys
input = sys.stdin.readline

def count_ways_to_steal():
    count = 0
    money = sum(houses[:m])
    
    if money < k: count += 1
    
    # n 과 m이 같은 경우, 한가지 경우만 고려
    if n == m: return count
    
    left, right = 0, m
    for _ in range(n-1):
        money += houses[right] - houses[left]
        if money < k: count += 1 # 방법장치 작동안하는 경우
        right = (right + 1) % n
        left = (left + 1) % n
    
    return count

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        houses = list(map(int, input().split()))
        print(count_ways_to_steal())