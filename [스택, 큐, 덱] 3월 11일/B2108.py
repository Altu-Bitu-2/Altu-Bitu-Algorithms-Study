import sys, collections
input = sys.stdin.readline

def solution():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    
    # 산술평균
    print(round(sum(numbers) / n))

    # 중앙값
    numbers.sort()
    print(numbers[n//2])

    # 최빈값
    cnt = collections.Counter(numbers)
    sorted_cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

    num, cnt = sorted_cnt[0]
    if n != 1:
        if sorted_cnt[1][1] == cnt:
            num = sorted_cnt[1][0]
    print(num)

    # 범위
    print(numbers[-1] - numbers[0])

if __name__ == "__main__":
    solution()