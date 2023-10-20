import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

minA = N * M


def check_board(row, col, N, M):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    ans = 0
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            for t in range(4):
                ni = row + di[t]
                nj = col + dj[t]

                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] == arr[row][col]:
                        ans += 1

                        if ans >= minA:
                            return
                

