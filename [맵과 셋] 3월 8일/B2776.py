import sys
input = sys.stdin.readline

def solution():
    
    t = int(input())
    while t > 0:
        t-=1
        n = int(input())
        note1 = set(map(int, input().split()))
        
        m = int(input())
        note2 = list(map(int, input().split()))
        
        for i in range(m):
            if note2[i] in note1:
                print("1")
            else:
                print("0")

if  __name__ == "__main__":
    solution()