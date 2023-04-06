import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [[0]*N for _ in range(N)]
cnt = 0

def promising(i, j):

    # 위, 좌상, 우상에 없으면 유망
    di = [-1, -1, -1]
    dj = [0, -1, 1]

    # 3방향에 대해 조사
    for k in range(3):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj]:
                return 0
    # 세 방향 모두에서 없어야함!!!
    return 1


# 0행부터 내려감, 끝나는 기준=N
def DFS(i, N):

    global cnt

    if i == N:
        cnt += 1
        return

    for j in range(N):
        # 해당 위치가 유망하다면 두고 다음 행 조사
        if promising(i, j):
            arr[i][j] = 1
            DFS(i+1, N)
            arr[i][j] = 0

DFS(0, N)
print(cnt)