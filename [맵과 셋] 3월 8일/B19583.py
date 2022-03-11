import sys
input = sys.stdin.readline

def solution():
    s, e, q = input().split()

    cnt = 0
    attendees = set()
    
    # 입력 개수 모를 때
    while True:
        try:
            time, nickname = input().split()
            
            if time <= s:
                attendees.add(nickname)
            elif e <= time <= q:
                if nickname in attendees:
                    attendees.discard(nickname)
                    cnt += 1

        except:
            break
    
    print(cnt)
    
if __name__ == "__main__":
    solution()