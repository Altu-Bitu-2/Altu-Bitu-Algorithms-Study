import sys
input=sys.stdin.readline

def solution():
    a, b = map(list, input().split())
    
    a.reverse()
    b.reverse()
    if len(a) < len(b):
        a += [0] * (len(b) - len(a))
    else:
        b += [0] * (len(a) - len(b))
    
    ans = []
    up = 0
    for u, v in zip(a, b):
        u, v = map(int, (u, v))
        sum_two = u + v + up
        if sum_two > 9:
            sum_two -= 10
            up = 1
        else:
            up = 0
        ans.append(str(sum_two))
        
    if up == 1:
        ans.append("1")

    print("".join(reversed(ans)))
        
if __name__ == "__main__":
    solution()