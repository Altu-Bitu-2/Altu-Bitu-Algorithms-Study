import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    dic = {}
    while n > 0:
        n -= 1
        
        file_name = input()
        _, ext = file_name.strip().split('.')
        if ext not in dic:
            dic[ext] = 1
        else:
            dic[ext] += 1
        
    for ext, cnt in sorted(dic.items()):
        print(ext, cnt)

if __name__ == "__main__":
    solution()