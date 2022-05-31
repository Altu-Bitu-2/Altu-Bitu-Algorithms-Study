import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

"""
 [거짓말]

 1. 각 사람들은 다양한 파티를 통해 연결됐다고 할 수 있음
 2. 연결된 사람들은 같은 집합에 속함
 3. 각 집합에 속한 사람들 중 한 명이라도 진실을 안다면 그 집합의 사람들이 속한 파티에는 거짓말을 할 수 없음
 -> 유니온 파인드로 사람들을 집합으로 묶은 뒤, 파티마다 거짓말을 할 수 있는지 확인하기
 -> 이때, 진실을 아는 사람들의 루트 정점을 0으로 설정해서 유니온 파인드를 통해 집합으로 묶고 시작
 -> 0과 같은 집합이 아니어야 거짓말을 할 수 있음

 !주의! 파티 정보를 입력받으며 바로 거짓말 가능 여부를 판단할 수 없음 (예제 입력 4)
       각 파티에서 한 사람만 저장해둔 뒤, 마지막에 거짓말 가능 여부 한 번에 판단
"""
# Weighted Union Find
# find 연산
def find_parent(x): # x의 루트 정점을 반환하는 함수
    if parent[x] < 0: # 해당 정점이 루트 정점
        return x # 해당 정점을 반환
    parent[x] = find_parent(parent[x]) # 부모를 루트 정점으로 설정
    return parent[x] # x의 부모를 반환

# union 연산
def union(x, y): # 두 정점 번호를 매개변수로 받아 union 연산을 하는 함수
    px = find_parent(x) # 정점 x의 루트 정점 구하기
    py = find_parent(y) # 정점 y의 루트 정점 구하기

    if px == py: # 루트 정점이 같은 경우
        return # 같은 집합에 속하므로 바로 반환

    if parent[px] < parent[py]: # 정점 x의 루트 정점에 저장된 정점의 수가 정점 y의 루트 정점보다 많은 경우
        parent[px] += parent[py] # 정점 x의 루트 정점에 저장된 정점의 수에 정점 y의 루트 정점의 정점의 수 더하기
        parent[py] = px  # 정점 y의 루트 정점의 부모 정점을 정점 x의 루트 정점으로 설정
    else: # 아니라면
        parent[py] += parent[px] # 정점 y의 루트 정점의 저장된 정점의 수에 정점 x의 루트 정점의 정점의 수 더하기
        parent[px] = py # 정점 x의 루트 정점의 부모 정점을 정점 y의 루트 정점으로 설정
    return # 반환

def count_liar_party(party): # 각 파티의 대표자 배열을 매개변수로 받아 각 파티의 대표자가 진실을 아는 사람이 아닌지 확인하여 과장된 이야기를 할 수 있는 파티 개수의 최대값을 반환하는 함수
    cnt = 0 # 과장된 이야기를 할 수 있는 파티 개수 변수 0으로 초기화

    for i in party: # 각 파티 대표자에 대해
        if find_parent(i) != find_parent(0): # 부모 정점이 0이 아니라면
            cnt += 1 # 과장된 이야기를 할 수 있는 파티 개수 1 증가
    
    return cnt # 과장된 이야기를 할 수 있는 파티 개수 최대값 반환

# 입력
n, m = map(int, input().split()) # 사람의 수, 파티의 수
parent = [-1] * (n+1)     # 루트 정점 초기화

party = []  # 각 파티의 대표자 저장할 리스트

# 진실을 아는 사람들
for i in map(int, input().split()[1:]): # 모든 진실을 아는 사람들에 대해
    union(i, 0) # 루트 정점을 0으로 설정된 집합으로 묶고 시작

# 각 파티에 대한 입력 & 연산
for _ in range(m): # 각 파티에 대해
    arr = list(map(int, input().split())) # 각 파티마다 오는 사람의 수와 번호를 리스트에 저장
    party.append(arr[1])    # 파티 정보로 각 파티의 첫번째 사람만 저장 # 각 모임의 대표자
    for i in range(2, arr[0] + 1): # 첫번째 사람을 제외한 모든 파티 참여자들에 대해
        union(arr[i], arr[1]) # 첫번째 사람과 같은 집합으로 묶기

# 연산 & 출력
print(count_liar_party(party)) # 과장된 이야기할 수 있는 파티 개수 최대값을 반환하는 함수 호출 후 출력