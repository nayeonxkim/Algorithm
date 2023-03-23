import sys
sys.stdin = open('input.txt')

def kill_fly(arr):

    # 분사력에 따라 방향제어 배열 생성
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    max_ans = 0
    for i in range(N):
        for j in range(N):
            row, col = i, j
            # ans1은 대각선, ans2는 상하좌우
            ans1 = ans2 = arr[row][col]
            for k in range(8):
                for m in range(1, M):
                    ni = row + di[k] * m
                    nj = col + dj[k] * m
                    if 0 <= ni < N and 0 <= nj < N:
                        if k % 2:   # 홀수면
                            ans1 += arr[ni][nj]
                        else:
                            ans2 += arr[ni][nj]

            if max_ans < max(ans1, ans2):
                max_ans = max(ans1, ans2)
    return max_ans


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, -1, 0, 1, 1, 1, 0, -1] * (M - 1)
    dj = [0, 1, 1, 1, 0, -1, -1, -1] * (M - 1)

    ans = kill_fly(arr)
    print(f'#{tc} {ans}')