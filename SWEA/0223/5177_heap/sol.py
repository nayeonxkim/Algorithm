'''
최소 이진힙 코드로 트리 만들고
루트노드까지 부모 찾아가면서 key더하기
부모노드가 0일때까지
c//2

'''


def enq(n):
    global last

    # 완전이진트리에 정점 추가
    last += 1
    # 마지막 정점(last)에 숫자를 인큐한다.
    heap[last] = n

    c = last  # 마지막 정점을 자식노드로 두고
    p = c // 2  # 완전이진트리이므로 단순히 나누기 2를 해서 부모노드를 구한다.

    # 부모가 있고, key값이 부모 < 자식이면 자리를 바꾼다.
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    return



import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    heap = [0] * (N+1)


    last = 0

    for n in numbers:
        enq(n)

    ans = 0
    c = last
    p = c // 2
    while p > 0:
        ans += heap[p]
        p //= 2

    print(f'#{tc} {ans}')