import sys
input = sys.stdin.readline
output = sys.stdout.write

def find_lower_bound(target, left, right):
    if left > right: return left
    
    mid = (left + right) // 2
    if cards[mid] == target:
        return find_lower_bound(target, left, mid-1)
    elif cards[mid] > target:
        return find_lower_bound(target, left, mid-1)
    else: return find_lower_bound(target, mid+1, right)
    
def find_upper_bound(target, left, right):
    if left > right: return right
    
    mid = (left + right) // 2
    if cards[mid] == target:
        return find_upper_bound(target, mid+1, right)
    elif cards[mid] > target:
        return find_upper_bound(target, left, mid-1)
    else: return find_upper_bound(target, mid+1, right)
        
def solution():
    cards.sort()
    ans = []
    for x in targets:
        upper_bound = find_upper_bound(x, 0, n-1)
        lower_bound = find_lower_bound(x, 0, n-1)
        ans.append(upper_bound - lower_bound + 1)
    output(" ".join(map(str, ans)))

if __name__=="__main__":
    n = int(input())
    cards = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))
    
    solution()