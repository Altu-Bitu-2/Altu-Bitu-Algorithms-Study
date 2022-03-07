import sys, re
input = sys.stdin.readline

def sum_digits(serial_number):

    numbers = re.findall(r'\d', serial_number)
    result = sum(map(int, numbers))
    
    return result
    
def solution():
    n = int(input())
    
    # guiter = []
    # for _ in range(n):
    #     guiter.append(input().strip())
    
    guiter = [input().strip() for _ in range(n)]

    guiter.sort(key=lambda x: (len(x), sum_digits(x), x))
    
    for serial_number in guiter:
        print(serial_number)
    
if __name__ == "__main__":
    solution()