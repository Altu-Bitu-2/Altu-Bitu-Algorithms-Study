import sys
input = sys.stdin.readline

def solution():
    brackets = input().strip()
    stack = []
    matching_dic = {']': '[', ')': '('}
    value_dic = {'[': 3, '(': 2, ']': 3, ')': 2}
    
    result = 0
    tmp = 1
    
    for i in range(len(brackets)):
        if brackets[i] in ('[', '('):
            stack.append(brackets[i])
            tmp *= value_dic[brackets[i]]
            
        elif brackets[i] in (']', ')'):
            if not stack or stack[-1] != matching_dic[brackets[i]]:
                result = 0
                break
            if brackets[i-1] == matching_dic[brackets[i]]:
                result += tmp
            stack.pop()
            tmp //= value_dic[brackets[i]]
    
    if stack:
        result = 0

    print(result)
            
if __name__ == "__main__":
    solution()