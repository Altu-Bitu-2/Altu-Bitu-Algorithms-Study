import sys
input = sys.stdin.readline

def solution():
    card = [i for i in range(1, 21)]

    for _ in range(10):
        a, b = map(int, input().split())
        for i in range(b, a, -1):
            for j in range(a, i):
                tmp = card[j]
                card[j] = card[j-1]
                card[j-1] = tmp
            
    for c in card:
        print(c, end=' ')
    print()
        
if __name__ == "__main__":
    solution()