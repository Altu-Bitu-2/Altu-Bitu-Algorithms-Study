import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    customers = []
    for _ in range(n):
        customers.append(int(input()))
    
    customers.sort(reverse=True)
    
    result = 0
    for i, c in enumerate(customers):
        if c-i < 0:
            break
        result += c-i
    
    print(result)
    
    
    
if __name__ == "__main__":
    solution()