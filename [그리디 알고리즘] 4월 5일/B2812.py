import sys
input = sys.stdin.readline

def solution():
    cnt = k
    
    stack = []
    for num in number:
        # 앞 숫자가 작은 경우, 앞 숫자 pop
        while stack and cnt and stack[-1] < num:
            stack.pop()
            cnt -= 1
        stack.append(num)
    
    # 끝 부분의 작은 수 제외한 문자열 반환
    return ''.join(stack[:n-k])

if __name__ == "__main__":
    n, k = map(int, input().split())
    number = list(input().strip())
    print(solution())