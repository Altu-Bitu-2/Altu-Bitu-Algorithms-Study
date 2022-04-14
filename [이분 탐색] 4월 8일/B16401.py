import sys
input = sys.stdin.readline
output = sys.stdout.write

def count_nephew(length):
    cnt = 0
    for i in l:
        if i >= length: cnt += (i//length)
    return cnt

def binary_search(target, left, right):
    if left > right: return right
    mid = (left + right) // 2
    if count_nephew(mid) >= target:
        return binary_search(target, mid+1, right)
    else: return binary_search(target, left, mid-1)

if __name__ == "__main__":
    m, n = map(int, input().split())
    l = list(map(int, input().split()))
    
    # 나눠줄 수 있는 조카 수가 n이 되는 최대 길이 k 구하기
    l.sort()
    output(str(binary_search(m, 1, max(l))))
    