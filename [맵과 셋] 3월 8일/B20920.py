import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    dic = {}
    for _ in range(n):
        word = input().strip()
        if len(word) < m:
            continue
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
        
    [print(word) for word, _ in sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]

if __name__ == "__main__":
    solution()