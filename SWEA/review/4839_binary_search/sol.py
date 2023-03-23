import sys
sys.stdin = open('input.txt')

def binary_search(page, key):
    l = 1
    r = page
    cnt = 1
    c = int((l + r) / 2)

    while c != key:
        if c > key:
            r = c
        else:
            l = c
        cnt += 1
        c = int((l + r) / 2)
    return cnt


T = int(input())
for tc in range(1, T+1):
    page, A, B = map(int, input().split())

    ans1 = binary_search(page, A)
    ans2 = binary_search(page, B)

    if ans1 < ans2:
        ans = 'A'
    elif ans1 > ans2:
        ans = 'B'
    else:
        ans = 0

    print(f'#{tc} {ans}')

