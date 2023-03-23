import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    for n in range(1, N):
        if n ** 3 == N:
            ans = n
            break
        elif n ** 3 > N:
            ans = -1
            break
    else:
        ans = -1

    print(f'#{tc} {ans}')