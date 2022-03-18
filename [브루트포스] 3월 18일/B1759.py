import sys
from itertools import combinations
input = sys.stdin.readline
            
def solution():
    consonant = {'a', 'e', 'i', 'o', 'u'}
    l, _ = map(int, input().split())
    characters = list(input().split())
    
    passwords = []
    for case in combinations(characters, l):
        tmp = len(set(case) & consonant)
        if 1 <= tmp <= l-2:
            case = sorted(list(case))
            passwords.append("".join(case))
        
    [print(pw) for pw in sorted(passwords)]
          
if __name__ == "__main__":
    solution()