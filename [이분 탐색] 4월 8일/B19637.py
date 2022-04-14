import sys
input = sys.stdin.readline
output = sys.stdout.write

def binary_search(target, left, right):
    if left > right: return left
    
    mid = (left + right) // 2
    
    if power_limits[mid][1] == target:
        return binary_search(target, left, mid-1)
    elif power_limits[mid][1] < target:
        return binary_search(target, mid+1, right)
    else:
        return binary_search(target, left, mid-1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    power_limits = []
    for _ in range(n):
        title, limit = input().split()
        power_limits.append((title, int(limit)))

    MAX = max([x[1] for x in power_limits])
    
    for _ in range(m):
        idx = binary_search(int(input()), 0, n-1)
        output(power_limits[idx][0] + "\n")