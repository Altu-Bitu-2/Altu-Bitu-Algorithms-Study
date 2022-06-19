import sys
input = sys.stdin.readline

def solution(gender, number):
    if gender == 2: # 여학생
        switches[number-1] = 1 - switches[number-1] # 받은 번호 switching
        
        limit = min(switch_number - number, number - 1) # 좌우로 가능한 범위 구하기
        for diff in range(1, limit+1): # 좌우로 대칭이면 스위칭
            left, right = number - 1 - diff, number - 1 + diff # 좌우
            if switches[left] != switches[right]: break # 대칭이 아니면 break
            switches[left] = 1 - switches[left]
            switches[right] = 1 - switches[right]
    else: # 남학생
        for idx in range(number-1, switch_number, number): # 배수인 번호 switching
            switches[idx] = 1 - switches[idx]

if __name__ == "__main__":
    switch_number = int(input()) # 스위치 개수
    switches = list(map(int, input().split())) # 스위치 상태
    student_number = int(input()) # 학생수
    # 스위치: 1 - 켜져 있음, 0 - 꺼져 있음``
    # 남: 받은 수의 배수의 스위치 상태 변경
    # 여: 좌우 대칭 최대 구간 스위치 상태 변경
    # 한 학생의 성별, 학생이 받은 수 (1 - 남학생, 2 - 여학생)
    
    for _ in range(student_number):
        gender, number = map(int, input().split())
        solution(gender, number)
    
    for i in range(0, switch_number, 20):
        print(" ".join(map(str, switches[i:i+20])))