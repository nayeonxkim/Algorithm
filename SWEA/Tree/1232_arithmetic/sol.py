import sys
sys.stdin = open('input.txt')

def postorder(node):
    if node != 0:
        postorder(left[node])
        postorder(right[node])

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

    arr = [list(input().split()) for _ in range(N)]

    for lst in arr:
        idx = int(lst[0])

        if lst[1] in '*+-/':
            tree[idx] = lst[1]
        else:
            tree[idx] = int(lst[1])

        if len(lst) == 4:
            left[idx] = int(lst[2])
            right[idx] = int(lst[3])
        elif len(lst) == 3:
            left[idx] = int(lst[2])

    postorder(1)
    print(f'#{tc} {int(tree[1])}')
