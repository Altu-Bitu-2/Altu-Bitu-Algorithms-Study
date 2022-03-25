import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    
    cnt = 0
    
    for _ in range(n):
        word = input().strip()
        stack = [word[0]]
        is_group = True
        
        # 단어의 모든 문자에 대해서
        for i in range(1, len(word)):
            if stack[-1] == word[i]:
                continue
            else:  # stack의 탑이 문자와 다르다면
                if word[i] in stack: # 이미 stack에 존재하는 문자라면, 그룹단어 아님
                    is_group = False
                    break
                else: # 아니라면, 새로운 문자를 stack에 넣기
                    stack.append(word[i])
        if is_group: # 그룹 단어였다면 cnt 1 증가
            cnt += 1
        
    print(cnt)      

if __name__ == "__main__":
    solution()