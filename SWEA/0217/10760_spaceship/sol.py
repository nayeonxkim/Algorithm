import sys
sys.stdin = open('input.txt')

def spaceship(arr):

    global N
    global M

    di = [-1, 1, 0, -1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    candidates = 0

    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] < arr[i][j]:
                        cnt += 1

            if cnt >= 4:
                candidates += 1

    return candidates

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    ans = spaceship(arr)
    print(f'#{tc} {ans}')