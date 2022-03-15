import sys
input = sys.stdin.readline

def solution():
    alpha = [0] * 26    
    name = input().strip()

    for c in name:
        alpha[ord(c)-65] += 1
    
    odd_cnt = 0
    half_str = ''
    odd_str = ''
    
    for i in range(26):
        half_str += chr(i+65) * (alpha[i]//2)
        
        if alpha[i] % 2 == 1:
            odd_cnt += 1
            odd_str = chr(i+65)
        
    if odd_cnt <= 1:
        print(half_str + odd_str + half_str[::-1])
    else:
        print("I'm Sorry Hansoo")            
    
if __name__ == "__main__":
    solution()