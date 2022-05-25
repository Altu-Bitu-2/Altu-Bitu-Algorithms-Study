import sys
input = sys.stdin.readline

def simulate(i, s):
    # 게시된 학생이 추천 받는 경우
    if s in frames:
        frames[s][0] += 1
        
    # 게시된 학생이 아닌 경우
    else: 
        # 빈 사진틀이 없는 경우
        # 추천 횟수 최소, 추천 시간 최소인 학생
        # 사진틀에서 삭제
        if len(frames) >= n: 
            candidates = sorted(frames.items(), key = lambda x: x[1])
            t = candidates[0][0] # 삭제할 학생
            del frames[t]
            
        # 사진틀에 새 학생 게시
        frames[s] = [1, i]

if __name__ == "__main__":
    n = int(input()) # 사진틀 개수
    
    frames = dict()
    m = int(input()) # 전체 학생들 추천 횟수
    
    # 추천 받은 순서대로 시뮬레이션
    for i, s in enumerate(map(int, input().split())):
        simulate(i, s)
        
    print(" ".join(map(str, sorted(frames.keys()))))