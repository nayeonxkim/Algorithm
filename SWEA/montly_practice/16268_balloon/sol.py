import sys
sys.stdin = open('input.txt')

def pang(arr):

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_ans = 0
    for i in range(N):
        for j in range(M):
            row, col = i, j
            ans = arr[row][col]
            for k in range(4):
                ni = row + di[k]
                nj = col + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    ans += arr[ni][nj]

            if max_ans < ans:
                max_ans = ans

    return max_ans


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = pang(arr)
    print(f'#{tc} {res}')
