import sys
sys.stdin = open('input.txt')

def backtrack(i, N, B, H):
    global minD

    # 가지치기
    if H - B >= minD:
        return

    # 종료조건
    if i == N:
        D = H - B
        if D >= 0:
            minD = min(minD, D)
        return

    backtrack(i+1, N, B, H + arr[i])
    backtrack(i + 1, N, B, H)


T= int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    minD = 20 * 10000

    backtrack(0, N, B, 0)
    print(f'#{tc} {minD}')