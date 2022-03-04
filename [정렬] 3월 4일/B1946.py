import sys
input = sys.stdin.readline

def solution():
    t = int(input())
    
    while t > 0:
        t-=1
        n = int(input())
        applicants = []
        for i in range(n):
            resume, interview = map(int, input().split())
            applicants.append((resume, interview))
        
        applicants.sort()
        
        cnt = 1
        pre = applicants[0][1]
        for i in range(1, n):
            if applicants[i][1] == 1:
                cnt += 1
                break
            if pre > applicants[i][1]:
                pre = applicants[i][1]
                cnt += 1 
        
        print(cnt)   
        
if __name__ == "__main__":
    solution()