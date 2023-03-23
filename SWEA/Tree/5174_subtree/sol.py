import sys
sys.stdin = open('input.txt')

def postorder(node):
    global cnt
    if node != 0:
        postorder(left[node])
        postorder(right[node])
        cnt += 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    left = [0] * (E+2)
    right = [0] * (E+2)

    lst = list(map(int, input().split()))

    for i in range(E):
        p, c = lst[i*2], lst[i*2+1]

        if not left[p]:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    postorder(N)
    print(f'#{tc} {cnt}')