# 2866_N_Queen
# 유망한자리인지= 같은 행, 열, 대각선에 퀸이 없는지 확인
def promising(i, j):
    # 0행 부터 놓기때문에 위로만 신경쓰면 됨
    # 같은 행인 애들은 따로 검사하니까 열은 조사 X
    # 위, 좌상 대각선, 우상 대각선
    di = [-1, -1, -1]
    dj = [0, -1, 1]

    # 상하좌우 탐색
    for k in range(3):
        ni = i + di[k]
        nj = j + dj[k]

        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj]:   # 내 상하좌우에 다른 퀸이 있다면
                return 0

            # 없다면 해당 방향으로 쭉 더 간다.
            ni += di[k]
            nj += dj[k]

    return 1 # 쭉 다 탐색했는데 다른 퀸이 없으면 유망한 자리


def BackTrack(i, N):
    global cnt
    if i == N:  # 모든 퀸을 보드에 다 놓았다면
        cnt += 1 # 경우의 수 +1
    else:
        for j in range(N):
            # i, j에 대해 해당 칸이 유망하다면
            if promising(i, j):
                # 퀸을 그 자리에 놓고
                board[i][j] = 1
                # 다음 행에 대해 같은 과정 반복
                BackTrack(i+1, N)
                # 원위치시키고 이번 행의 다른 경우를 조사하러갈거
                board[i][j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    board = [[0]*N for _ in range(N)]
    cnt = 0         # 놓을 수 있는 경우의 수
    BackTrack(0, N) # 0번 행부터 퀸을 놓는다.

    print(f'#{tc} {cnt}')