import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [[0]*N for _ in range(N)]
cnt = 0

def promising(i, j):
    # 내 위치에서 위, 좌상, 우상쭉에 모두 퀸이 없으면 True
    di = [-1, -1, -1]
    dj = [0, -1, 1]

    # 현재 위치를 표시
    r, c = i, j
    # 방향 의미
    k = 0
    while 0 <= r and 0 <= c < N:
        while not arr[r][c]:
            r += di[k]
            c += dj[k]





def backtrack(i, N):
    global cnt

    if i == N-1:
        cnt += 1
        return


    for j in range(N):
        if promising(i, j):
            arr[i][j] = 1
            backtrack(i+1, N)
            arr[i][j] = 0