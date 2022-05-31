import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""
 [사이클 게임]

 사이클이 발생한 순간 = 같은 집합에 있는 원소 두 개를 유니온하려 할 때
 union 함수의 리턴값을 boolean으로 주어 cycle이 생성되는 순간 발견하기
"""
# Weighted Union Find
# find 연산
def find_parent(x): # x의 원소 정점을 반환하는 함수
    if parent[x] < 0: # 해당 원소가 루트 원소
        return x # 해당 원소을 반환
    parent[x] = find_parent(parent[x]) # 부모를 루트 원소로 설정
    return parent[x] # x의 부모를 반환

# union 연산
def union(x, y): # 두 원소를 매개변수로 받아 같은 집합에 있으면 False 반환하고 아니면 union하고 True 반환
    px = find_parent(x) # 원소 x의 루트 원소 구하기
    py = find_parent(y) # 원소 y의 루트 원소 구하기

    if px == py: # 루트 정점이 같은 경우
        return False # 사이클이 발생하므로 False 반환

    if parent[px] < parent[py]: # 원소 x의 루트 원소에 저장된 원소의 수가 원소 y의 루트 원소보다 많은 경우
        parent[px] += parent[py] # 원소 y의 루트 원소에 저장된 원소의 수가 원소 y의 루트 원소의 정점의 수 더하기
        parent[py] = px # 원소 y의 루트 원소의 부모 원소를 원소 x의 루트 정점으로 설정
    else: # 아니라면
        parent[py] += parent[px] # 원소 y의 루트 원소의 저장된 원소의 수에 원소 x의 루트 원소의 원소의 수 더하기
        parent[px] = py # 원소 x의 루트 원소의 부모 원소를 원소 y의 루트 정점으로 설정

    return True # 루트 정점이 같지 않은 경우 True 반환

# 입력
n, m = map(int, input().split()) # 점의 개수, 차례의 수
parent = [-1]*n     # 초기화 # 부모 리스트 -1로 초기화

for i in range(m): # i: 0, 1, ... , m-1 에 대해
    x, y = map(int, input().split()) # 플레이어가 선택한 두 점의 번호
    if not union(x, y): # 만약 사이클이 발생하였다면
        # 사이클이 생성됨
        print(i+1) # 사이클이 처음으로 만들어진 차례의 번호(i + 1) 출력
        break # 게임 종료
else:   # for-else문: for문이 break에 걸리지 않고 정상 종료된 경우에만 else문 실행 # m번 동안 사이클이 발생하지 않았다면
    print(0) # 0 출력