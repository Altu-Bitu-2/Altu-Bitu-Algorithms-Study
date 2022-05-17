import sys
input = sys.stdin.readline

def solution():
    
    section = 2 * k + 1
    max_val = subtotal = sum(buckets[:section])
    
    # end_point가 section 보다 작은 경우
    # section = 3
    # 0 1 2
    # 0 5 2

    # section = 7
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    # 0 5 2 4 0 0 0 4 0 0 0  0  0  0  0  10
    # 부분합 : buckets[i] ~ buckets[i + section -1]
    # i = 0 ... end_point - section + 1
    
    for i in range(end_point - section + 1):
        subtotal += (buckets[i + section] - buckets[i])
        max_val = max(max_val, subtotal)
    
    return max_val
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    buckets = [0] * (int(1e6) + 1)
    end_point = 0
    for _ in range(n):
        g, x = map(int, input().split())
        buckets[x] = g
        end_point = max(end_point, x)
        
    print(solution())