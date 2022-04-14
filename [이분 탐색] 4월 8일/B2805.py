import sys
input = sys.stdin.readline
output = sys.stdout.write

def calculate_tree(height):
    result = 0
    for i in h:
        if i > height: result += (i-height)
    return result

def binary_search(target, left, right):
    if left > right: return right
    mid = (left + right) // 2
    if calculate_tree(mid) >= target:
        return binary_search(target, mid+1, right)
    else: return binary_search(target, left, mid-1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    
    # 나눠줄 수 있는 조카 수가 n이 되는 최대 길이 k 구하기
    h.sort()
    output(str(binary_search(m, 0, max(h))))
    