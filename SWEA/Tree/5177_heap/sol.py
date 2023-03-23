import sys
sys.stdin = open('input.txt')

# 어떤 노드에 인큐하길 바라는 값을 입력값으로 한다.
def heap(n):

    global last

    # 값 할당하기
    last += 1
    tree[last] = n

    c = last
    p = c // 2

    while p > 0 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2
    return



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    tree = [0] * (N+1)

    last = 0
    for n in data:
        heap(n)

    # 마지막 정점의 조상노드들의 합
    c = last
    p = c//2
    ans = 0
    while p != 0:
        ans += tree[p]
        c = p
        p = c//2

    print(f'#{tc} {ans}')