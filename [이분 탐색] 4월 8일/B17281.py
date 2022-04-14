import sys
from itertools import permutations
input = sys.stdin.readline
output = sys.stdout.write

def solution():
    ans = 0
    
    for case in permutations([i for i in range(1, 9)], 8):
        case = list(case[:3]) + [0] + list(case[3:])
        score, idx = 0, 0        
        for inning in innings:
            out = 0
            base1, base2, base3 = 0, 0, 0
            while out != 3:
                if inning[case[idx]] == 1:
                    score += base3
                    base1, base2, base3 = 1, base1, base2
                elif inning[case[idx]] == 2:
                    score += base2 + base3
                    base1, base2, base3 = 0, 1, base1
                elif inning[case[idx]] == 3:
                    score += base1 + base2 + base3
                    base1, base2, base3 = 0, 0, 1
                elif inning[case[idx]] == 4:
                    score += base1 + base2 + base3 + 1
                    base1, base2, base3 = 0, 0, 0 
                else: out += 1
                
                idx = (idx + 1) % 9
                
        ans = max(score, ans)
        
    return str(ans)

if __name__ == "__main__":
    n = int(input())
    innings = [list(map(int, input().split())) for _ in range(n)]
    
    output(solution())