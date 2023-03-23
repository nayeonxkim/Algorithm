import sys
sys.stdin = open('input.txt')

# 특정 노드부터 시작 = 루트 노드가 되는 번호
# inorder = 왼 나 오 (중위)
# preorder = 나 왼 오 (전위)
# postorder = 왼 오 나 (후위)
def inorder(node):
    if node != 0:

        # 왼쪽 자식노드
        inorder(left[node])

        # 자기자신 -> 논리
        print(tree[node], end = '')

        # 오른쪽 자식노드
        inorder(right[node])

for tc in range(1, 11):
    N = int(input())
    tree = [''] * (N+1)     # 트리의 정보
    left = [0] * (N+1)      # 왼쪽 자식 정보
    right = [0] * (N+1)     # 오른쪽 자식 정보
    # 1번 인덱스 = 1번 노드로 표현할 것이므로 N+1개씩 만든다.

    arr = [list(input().split()) for _ in range(N)]
    # 문자열로 입력받는다. -> int해주어야함

    for lst in arr:
        idx = int(lst[0])
        tree[idx] = lst[1]

        if len(lst) == 4:
            left[idx] = int(lst[2])
            right[idx] = int(lst[3])
        elif len(lst) == 3:
            left[idx] = int(lst[2])

    print(f'#{tc}', end = ' ')
    inorder(1)
    print()