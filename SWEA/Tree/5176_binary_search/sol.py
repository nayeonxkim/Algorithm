import sys
sys.stdin = open('input.txt')


def inorder(node):
    global val

    if node != 0:
        inorder(left[node])

        val += 1
        tree[node] = val

        inorder(right[node])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)


    # 왼쪽, 오른쪽 관계도 생성
    # 1번부터 N//2번까지 (부모가 될 수 있는 노드에 대하여) : 1~3
    # 자식 관계가 어떻게 되는지 정리한다.
    # 왼쪽 자식은 부모의 *2, 오른쪽 자식은 부모의 *2 +1
    # 그런데 오른쪽은 없을 수도 있기때문에, 주어진 노드 번호까지만 자식을 줌.
    for i in range(1, N//2 + 1):
        left[i] = i*2

        if i*2+1 <= N:
            right[i] = i*2 + 1

    # 재귀함수 안에다가 초기설정 (val=0)을 하면
    # 재귀가 호출될 때마다 0으로 리셋된다.
    # 따라서 전역변수로 초기설정을 해주고, global로 가져온다.
    val = 0
    inorder(1)

    root = tree[1]
    ans = tree[N//2]
    print(f'#{tc} {root} {ans}')