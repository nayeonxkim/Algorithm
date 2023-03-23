import sys
sys.stdin = open('input.txt')


def postorder(node):

    if node != 0:
        # 1. 왼쪽 자식노드
        postorder(left[node])
        # 2. 오른쪽 자식노드
        postorder(right[node])
        # 3. 자기자신
        if tree[node] == '-':
            tree[node] = tree[left[node]] - tree[right[node]]

        elif tree[node] == '+':
            tree[node] = tree[left[node]] + tree[right[node]]

        elif tree[node] == '*':
            tree[node] = tree[left[node]] * tree[right[node]]

        elif tree[node] == '/':
            tree[node] = tree[left[node]] / tree[right[node]]



for tc in range(1, 11):
    N = int(input())

    tree = [''] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        data = list(input().split())

        idx = int(data[0])

        if data[1].isdecimal():
            tree[idx] = int(data[1])
        else:
            tree[idx] = data[1]

        if len(data) == 4:
            left[idx] = int(data[2])
            right[idx] = int(data[3])
        elif len(data) == 3:
            left[idx] = int(data[2])


    # postorder(1)
    # print(f'#{tc} {int(tree[1])}')
    print(tree)