import sys
sys.stdin = open('input.txt')

def postorder(node):

        # 왼쪽
        postorder(node*2)

        # 오른쪽
        postorder(node * 2 + 1)

        # 자기자신에 두개 더한값
        # 역에 조건달아ㅣ파
        tree[node] = tree[node*2] + tree[node*2+1]


#
# def sum_of_node(L):
#     global last
#     p = L
#     c = p * 2  # 왼쪽 자식 번호
#
#     ans = 0
#     # 자식이 하나 이상 있으면
#     while c <= last:
#         if c + 1 <= last:
#             ans += tree[c]
#             c += 1
#
#
#     return ans



T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        i, tree[i] = map(int, input().split())


    postorder(1)
    print(tree)