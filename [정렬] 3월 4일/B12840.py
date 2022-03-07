import sys
input = sys.stdin.readline

S = 60
M = 60
H = 24

def cal_time(t, n, c):
    
    if t == 1:
        n += c
    else:
        n -= c
        
    n %= (H * M * S)
    
    h = n // (M * S)
    n %= (M * S)
    m = n // S
    n %= S
    return h, m, n
    
def solution():
    h, m, s = map(int, input().split())
    q = int(input())
    for i in range(q):
        query = input().rstrip()
        if len(query)==1:
             print(h, m, s)
        else:
            t, c = map(int, query.split())
            n = h * M * S + m * S + s
            h, m, s = cal_time(t, n, c)

if __name__ == "__main__":
    solution()