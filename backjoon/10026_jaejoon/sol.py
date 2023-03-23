import sys
sys.stdin = open('input.txt')


def color_block(arr, color):

    di = [0, 0, 1, -1]
    dj = [-1, 1, 0, 0]

    visited = [[0] * N for _ in range(N)]
    stack = []

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] in color and not visited[i][j]:
                stack.append((i, j))
                visited[i][j] = 1

                while stack:

                    row, col = stack.pop()

                    for k in range(4):
                        ni = row + di[k]
                        nj = col + dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] in color and not visited[ni][nj]:
                                stack.append((ni, nj))
                                visited[ni][nj] = 1
                cnt += 1
    return cnt

N = int(input())
arr = [list(input()) for _ in range(N)]

res = 0
for color in ['R', 'G', 'B']:
    res += color_block(arr, color)

res_blind = 0
for color in ['RG', 'B']:
    res_blind += color_block(arr, color)

print(res, res_blind)
