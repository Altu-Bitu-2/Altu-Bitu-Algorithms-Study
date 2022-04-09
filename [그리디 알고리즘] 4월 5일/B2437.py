import sys
input = sys.stdin.readline

def solution():

    # 오름차순 정렬
    weights.sort()
    
    end = 1 # 필요한 값
    for weight in weights:
        # 필요한 값보다 더 크다면
        if weight > end: return end
        end += weight
    
    return end

if __name__ == "__main__":
    n = int(input())
    
    weights = list(map(int, input().split()))
    print(solution())