import sys
input = sys.stdin.readline

def cal_time(t, n, c):
    
    if t == 1:
        n += c
    else:
        n -= c
        
    n %= (60 * 60 * 24)
    
    h = n//3600
    n %= 3600
    m = n//60
    n %= 60
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
            n = h * 60 * 60 + m * 60 + s
            h, m, s = cal_time(t, n, c)

if __name__ == "__main__":
    solution()