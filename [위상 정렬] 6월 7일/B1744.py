import sys
input = sys.stdin.readline

def sum_sorted_array(array):
    result = 0
    count = len(array)
    for i in range(0, count-1, 2):
        result += array[i] * array[i+1]
    if count % 2 == 1: result += array[-1]
    return result

def solution():
    positives = []
    negatives = []
    ones = 0
    
    for _ in range(n):
        number = int(input())
        if number > 1: positives.append(number)
        elif number <= 0: negatives.append(number)
        else: ones += 1

    positives.sort(reverse=True)
    negatives.sort()
    
    return sum_sorted_array(positives) + sum_sorted_array(negatives) + ones
    
if __name__ == "__main__":
    n = int(input())
    # 곱셈: (1 아닌 양수, 1 아닌 양수) (0 또는 음수, 0 또는 음수) 절대값 큰 순서대로
    # 덧셈: 1, 0, 남은 음수, 양수
    print(solution())