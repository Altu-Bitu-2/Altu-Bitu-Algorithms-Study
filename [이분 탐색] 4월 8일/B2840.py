import sys
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    
    checked = set()
    arr = [EMPTY] * n 
    idx = 0
    for _ in range(k):
        s, letter = input().split()
        s = int(s)
        idx = (idx - s) % n
        if arr[idx] == EMPTY and letter not in checked:
            arr[idx] = letter
            checked.add(letter)
        elif arr[idx] == letter: continue
        else: return WRONG
    
    return "".join(arr[idx:] + arr[:idx])

if __name__ == "__main__":
    EMPTY = "?"
    WRONG = "!"
    n, k = map(int, input().split())
    
    output(solution())