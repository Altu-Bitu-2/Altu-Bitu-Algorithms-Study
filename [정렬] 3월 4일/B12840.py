import sys
input = sys.stdin.readline

S = 60
M = 60
H = 24
def show_time(s):
    s %= (H * M * S)
    
    h = s // (M * S)
    s %= (M * S)
    m = s // S
    s %= S
    
    print(h, m, s)
    
def cal_time(t, n, c):
    if t == 1:
        n += c
    else:
        n -= c
    return n
    
def solution():
    h, m, s = map(int, input().split())
    n = h * M * S + m * S + s
    
    q = int(input())
    for i in range(q):
        query = input().rstrip()
        if len(query)==1:
             show_time(n)
        else:
            t, c = map(int, query.split())
            n = cal_time(t, n, c)

if __name__ == "__main__":
    solution()