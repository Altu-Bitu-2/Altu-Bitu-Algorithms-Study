import sys
input = sys.stdin.readline

def solution():
    infix = input().strip()
    stack = []
    ops = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 3}
    ans = ""
    
    for i in range(len(infix)):
        if infix[i].isalpha():
            ans += infix[i]
        else:
            if infix[i] == '(': # 여는 괄호는 무조건 스택에
                stack.append(infix[i])
            elif infix[i] == ')': # 닫는 괄호는 여는 괄호 만날 때까지 스택의 기호 출력
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                stack.pop() # ( 제거
            else: # 스택의 우선 순위 높은 기호 먼저 출력
                while stack and ops[stack[-1]] >= ops[infix[i]]:
                    ans += stack.pop()
                stack.append(infix[i])
    
    # 스택에 남은 기호 모두 출력
    while stack:
        ans += stack.pop()
            
    print(ans)

if __name__ == "__main__":
    solution()