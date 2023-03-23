import sys
sys.stdin = open('input.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = []

    for i in range(N-1):
        for j in range(M-1):
            cnt = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
                    ans.append(cnt)
    print(f'#{tc} {max(ans)}')