#  N과 M (12)
import sys
input = sys.stdin.readline

def backtracking(now):
    # 출력
    if len(l) == m:
        print(" ".join(map(str, l)))
        return
    
    pre = -1
    for i in range(now, n): # 비내림차순
        # 중복되는 순열 여러번 출력 x
        if pre == numbers[i]: continue 
        pre = numbers[i]

        l.append(numbers[i])
        backtracking(i) # 같은 수 선택 가능
        l.pop()
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort() # 비내림차순
    
    l = []
    backtracking(0)