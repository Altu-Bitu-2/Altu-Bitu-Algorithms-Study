import sys
input = sys.stdin.readline

def solution(n, info):
    max_score = -56 # 어피치 점수를 기준으로 라이언 최대 점수
    max_case =  [-1] # 최대 점수인 경우
    
    # 어피치 점수를 기준으로 라이언 점수 계산
    def get_score(arrow):
        total_score = 0
        for i in range(11):
            if arrow[i] > info[i]:
                total_score += (10 - i)
            elif arrow[i] < info[i]:
                total_score -= (10 - i)
        return total_score

    # 완전 탐색
    def dfs(score, left, arrow): # 쏘는 과녁 점수, 남은 화살 개수, 
        nonlocal max_score, max_case
        
        # 화살을 다 쏨
        if left < 0: return
        
        # 마지막 10점까지 탐색한 경우, 결과 확인
        if score == 11:
            # 라이언 점수 최대인지 확인
            lion_score = get_score(arrow)
            if lion_score <= 0: return
            elif lion_score > max_score:
                max_score = lion_score
                max_case = arrow[:10] + [left]
            return

        # 어피치보다 1 더 많이 쏘기
        tmp = info[10 - score] + 1 
        arrow[10 - score] = tmp
        dfs(score + 1, left - tmp, arrow)
        
        # 어피치에게 점수 주기
        arrow[10 - score] = 0
        dfs(score + 1, left, arrow)
    
    dfs(0, n, [0] * 11)
    return max_case
    
if __name__ == "__main__":

    # n = int(input())
    # info = list(map(int, input().split()))
    n = 5
    info =	[2,1,1,1,0,0,0,0,0,0,0]
    
    print(solution(n, info))