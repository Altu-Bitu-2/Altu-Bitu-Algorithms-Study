import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    while t > 0:
        t -= 1
        
        n = int(input())
        dic = {}
        for _ in range(n):
            _, type = input().strip().split()
            if type not in dic:
                dic[type] = 1
            else:
                dic[type] += 1
        
        result = 1
        for val in dic.values():
            result *= (val+1)
        result -= 1
        
        print(result)
    
if __name__ == "__main__":
    solution()