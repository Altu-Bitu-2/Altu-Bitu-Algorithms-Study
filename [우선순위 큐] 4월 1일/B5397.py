import sys
input = sys.stdin.readline

def solution(given_l):
    left_stack = []
    right_stack = []
    
    for l in given_l:
        if l == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif l == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        elif l == "-":
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(l)
    
    print("".join(left_stack) + "".join(reversed(right_stack)))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solution(input().strip())