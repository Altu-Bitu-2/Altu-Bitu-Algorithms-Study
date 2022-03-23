import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    
    cnt = 0
    
    for _ in range(n):
        word = input().strip()
        stack = [word[0]]
        is_group = True
        
        for i in range(1, len(word)):
            if stack[-1] == word[i]: # 만약 stack가 word와 다르다면
                continue
            else:
                if word[i] in stack:
                    is_group = False
                    break
                else:
                    stack.append(word[i])
        if is_group:
            cnt += 1
        
    print(cnt)      

if __name__ == "__main__":
    solution()