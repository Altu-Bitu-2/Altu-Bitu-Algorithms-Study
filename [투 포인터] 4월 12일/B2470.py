import sys
input = sys.stdin.readline

def two_pointer():
    liquid.sort()
    min_val = abs(liquid[0] + liquid[n-1])
    min_idx_1, min_idx_2 = 0, n-1
    left, right = 0, n-1
    while (left < right):
        tmp = liquid[left] + liquid[right]
        if abs(tmp) < min_val:
            min_val = abs(tmp)
            min_idx_1, min_idx_2 = left, right
        if tmp < 0: left += 1
        else: right -= 1
    print(liquid[min_idx_1], liquid[min_idx_2])

if __name__ == "__main__":
    n = int(input())
    liquid = list(map(int, input().split()))
    two_pointer()