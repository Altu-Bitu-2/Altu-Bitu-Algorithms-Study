import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 메모리 초과
# def get_postorder(preorder):

#     # 루트만 있거나 빈 리스트인 경우
#     if len(preorder) <= 1: return preorder
    
#     root = preorder[0]
#     left_right = preorder[1:]
    
#     # 왼쪽 오른쪽 나누기
#     for i in range(len(left_right)):
#         if left_right[i] > root: 
#             return get_postorder(left_right[:i]) + get_postorder(left_right[i:]) + [root]
    
#     # 오른쪽 없음
#     return get_postorder(preorder[1:]) + [root]

def get_postorder(left, right):
    
    if left >= right: return

    # left 와 right 구분
    mid = right
    for i in range(left+1, right):
        if preorder[i] > preorder[left]:
            mid = i
            break
    
    get_postorder(left+1, mid) # left
    get_postorder(mid, right) # right
    print(preorder[left]) # root
        
if __name__ == "__main__":
    preorder = []
    while True:
        try:
            preorder.append(int(input()))
        except:
            break

    get_postorder(0, len(preorder))