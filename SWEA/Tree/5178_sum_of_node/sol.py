import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        i, tree[i] = map(int, input().split())

    # 완전이진트리이기 때문에 부모노드 = 자식노드//2
    for i in range(N, 1, -1):
        tree[i//2] += tree[i]
    print(f'#{tc} {tree[L]}')