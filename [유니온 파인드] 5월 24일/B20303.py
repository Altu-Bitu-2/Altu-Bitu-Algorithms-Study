import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""
 [할로윈의 양아치] - pypy3로 제출

 - weighted union find -> 루트 정점에 아이들의 수(집합 원소 수)와 사탕 개수까지 쌍으로 저장하기
 - dp(냅색)으로 K명 미만의 아이들에게서 뺏을 수 있는 최대 사탕 수 구하기
"""
# Weighted Union Find
# find 연산
def find_parent(x): # x의 루트 정점을 반환하는 함수
    if parent[x][0] < 0: # 해당 정점이 루트 정점
        return x # 해당 정점을 반환
    parent[x][0] = find_parent(parent[x][0]) # 부모를 루트 정점으로 설정
    return parent[x][0] # x의 부모를 반환

# union 연산
def union(x, y): # 각 정점 번호를 매개변수로 받아 union 연산을 하는 함수
    px = find_parent(x) # 정점 x의 루트 정점 구하기
    py = find_parent(y) # 정점 y의 루트 정점 구하기

    if px == py: # 루트 정점이 같은 경우
        return # 같은 집합에 속하므로 바로 반환

    if parent[px][0] < parent[py][0]: # 정점 x의 루트 정점에 저장된 정점의 수가 정점 y의 루트 정점보다 많은 경우
        parent[px][0] += parent[py][0] # 정점 x의 루트 정점에 저장된 아이들의 수에 정점 y의 루트 정점의 아이들의 수 더하기
        parent[px][1] += parent[py][1] # 정점 x의 루트 정점의 사탕의 수에 정점 y의 루트 정점의 사탕의수 더하기
        parent[py][0] = px # 정점 y의 루트 정점의 부모 정점을 정점 x의 루트 정점으로 설정
    else: # 아니라면
        parent[py][0] += parent[px][0] # 정점 y의 루트 정점의 저장된 아이들의 수에 정점 x의 루트 정점의 아이들의 수 더하기기
        parent[py][1] += parent[px][1] # 정점 x의 루트 정점의 사탕의 수에 정점 y의 루트 정점의 사탕의수 더하기
        parent[px][0] = py # 정점 x의 루트 정점의 부모 정점을 정점 y의 루트 정점으로 설정
    return # 반환

def knapsack(k):
    dp = [0] * k    # 1부터 k-1까지 # 아이들의 수를 인덱스로, 최대 사탕의 수를 값으로 하는 dp 테이블 초기화
    count = []      # [아이들의 수, 사탕의 수] # 친구 집합을 저장할 리스트
    for p, c in parent: # -아이들의 수, 사탕의 수 # 각 아이에 대해
        if p < 0: # 루트 정점이라면
            count.append((-p, c)) # (아이들의 수, 사탕의 수)를 count 리스트에 저장
    
    for child_cnt, candy_cnt in count: # 각 친구 집합에 대해
        for i in range(k-1, child_cnt-1, -1): # k-1부터 해당 친구 집합의 아이들의 수까지의 인덱스에 대해
            dp[i] = max(dp[i], dp[i-child_cnt] + candy_cnt) # 해당 친구 집합을 포함한 경우와 포함하지 않은 경우의 최대값 계산

    return dp[-1] # 아이들의 수가 k-1인 경우의 사탕의 수의 최대값 반환

# 입력
n, m, k = map(int, input().split()) # 거리에 있는 아이들의 수, 아이들의 친구 관계 수, 울음소리가 공명하기 위한 최소 아이의 수
parent = [[-1, i] for i in map(int, ("0 "+input()).split())]    #[-아이들의 수, 사탕 개수] # 아이들이 받은 사탕의 개수를 parent 배열에 저장

for _ in range(m): # m개 만큼
    a, b = map(int, input().split()) # a, b는 친구 사이
    union(a, b) # 친구 사이는 같은 집합으로 묶기

# 연산 & 출력
print(knapsack(k)) # 울음소리가 공명하기 위한 최소 아이의 수를 인자로 주면, 최대로 뺏을 수 있는 사탕의 양 반환하는 함수 호출 후, 출력