import sys
from itertools import permutations
input = sys.stdin.readline

def cal_score(q_num, num):
    s = b = 0
    for i in range(3):
        if num[i] == q_num[i]: s += 1
        elif num[i] in q_num: b += 1
    return s, b
            
def solution():
    n = int(input())
    numbers = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))
    flag = [True] * len(numbers)
    
    for _ in range(n):
        q_num, s, b = input().split()
        s, b = map(int, (s, b))
        q_num = list(q_num)
        
        for i in range(len(numbers)):
            if not flag[i]: continue
            cal_s, cal_b = cal_score(q_num, numbers[i])
            if cal_s == s and cal_b == b: continue
            flag[i] = False
                
    print(flag.count(True))
    
if __name__ == "__main__":
    solution()