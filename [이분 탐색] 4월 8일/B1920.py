import sys
input = sys.stdin.readline

def binary_search(target, left, right):
    if left > right: return 0
    mid = (left + right) // 2
    
    if array[mid] == target:
        return 1
    elif array[mid] < target:
        return binary_search(target, mid+1, right)
    else:
        return binary_search(target, left, mid-1)
    
def solution():
    array.sort()
    results = [binary_search(x, 0, n-1) for x in targets]
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))
    
    solution()