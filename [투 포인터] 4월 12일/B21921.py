import sys
input = sys.stdin.readline

def solution():
    tmp = max_visitors = sum(visitors[:x])
    max_cnt = 1
    for i in range(n-x):
        tmp += (visitors[i + x] - visitors[i])
        if tmp > max_visitors:
            max_visitors = tmp
            max_cnt = 1
        elif tmp == max_visitors:
            max_cnt += 1
    if max_visitors:
        print(max_visitors)
        print(max_cnt)
    else:
        print("SAD")

if __name__ == "__main__":
    n, x = map(int, input().split())
    visitors = list(map(int, input().split()))
    solution()