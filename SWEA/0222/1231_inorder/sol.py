import sys
sys.stdin = open('input.txt')

# 중위
def inorder(node):
    if node != 0:
        inorder(left[node])
        print(tree[node], end = '')
        inorder(right[node])

for tc in range(1, 11):
    N = int(input())

    # 왼쪽/오른쪽 자식, 노드의 내용(문자)을 넣을 배열 생성
    left = [0] * (N+1)
    right = [0] * (N+1)
    tree = [''] * (N+1)

    # 리스트로 입력값 받음
    nodes = [list(input().split()) for _ in range(N)]

    # nodes 리스트의 길이에 따라 나누어 처리
    for i in range(N):
        num = int(nodes[i][0])

        # 1 W 2 3
        if len(nodes[i]) == 4:
            tree[num] = nodes[i][1]
            left[num] = int(nodes[i][2])
            right[num] = int(nodes[i][3])

        # 4 O 8
        elif len(nodes[i]) == 3:
            tree[num] = nodes[i][1]
            left[num] = int(nodes[i][2])

        # 5 T
        else:
            tree[num] = nodes[i][1]

    # 출력형식 맞추어 출력
    print(f'#{tc}', end = ' ')
    inorder(1)
    print()