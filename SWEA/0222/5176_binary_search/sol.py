import sys
sys.stdin = open('input.txt')

# 중위순회
def inorder(node):
    # 재귀호출 횟수
    inorder.counter += 1

    if node != 0:

        # 1. 왼쪽 자식노드
        inorder(left[node])

        # 2. 자기자신
        # tree배열에 자기자신노드까지의 재귀 호출 횟수를 저장
        tree[node] = inorder.counter

        # 3. 오른쪽 자식노드
        inorder(right[node])

    return tree

inorder.counter = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 각 노드안에 있는 값을 나타내줄 tree배열 생성
    tree = [0] * (N + 1)

    left = [0] * (N + 1)
    right = [0] * (N + 1)


## 트리 생성
    # 노드 안에 들어갈 값은 무시한 채로,
    # 노드의 번호만 가지고 왼쪽/오른쪽 자식노드 관계 생성
    # 1 -> 2/3, 2 -> 4/5번 노드
    # 2번 부터 6번까지 2씩 건너뛰면서 : 2, 4, 6
    for n in range(2, N+1, 2):
        # left[1] = 2, right[1] = 3
        left[n // 2] = n
        # 주어진 숫자보다 큰 값이 노드에 들어가면 안됨
        # -> N보다 작거나 같을 때까지만 노드 생성
        if n+1 <= N:
            right[n//2] = n+1

    res = inorder(1)
    # [0, 8, 5, 12, 4, 7, 11]
    res_idx = sorted(res)
    # [0, 4, 5, 7, 8, 11, 12]
    # -> 1번 노드의 값 = res_idx의 8의 인덱스 = 4
    
    # 1번 노드와 N//2번 노드의 값 출력
    root = res_idx.index(res[1])
    n_2 = res_idx.index(res[N//2])
    print(f'#{tc} {root} {n_2}')

