import sys
sys.stdin = open('input.txt')

def maze(arr):
    # 첫 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                row, col = i, j
    # 4행 3열이 2 -> row = 4, col = 3
    # row와 col은 현재 위치

    # 첫 시작점에 방문기록
    # 방문기록 = visited를 1로, stack에 해당 좌표 push
    visited[row][col] = 1
    stack.append((row, col))

    # 4방향 델타 값 설정 : 우, 상, 좌, 하
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 스택에 값이 있을 때까지만 반복
    while stack:
        # 시작점 설정
        row, col  = stack.pop()
        # stack에 튜플로 저장한 값을 각각 row와 col로 나누어 할당

        # 현재 위치가 도착점이면 1반환
        if arr[row][col] == 3:
            return 1

        # 현재 위치를 기준으로 4 방향을 탐색한다.
        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            # 배열의 범위를 벗어나지 않는다면,
            if 0 <= ni < N and 0 <= nj < N:
                # 해당 좌표가 방문기록이 없고, 벽에 막혀있지 않다면
                if visited[ni][nj] == 0 and arr[ni][nj] != 1:
                    # 방문기록을 남긴다. (갈 곳 목록에 남긴다.)
                    visited[ni][nj] = 1
                    stack.append((ni, nj))

    # stack이 빌 때까지 3에 도달하지 못해 함수가 실행되고 있다면,
    # 0을 반환한다.
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input()))

    # 갈 수 있는 곳을 쌓을 stack을 생성하고
    # 방문기록을 남길 visited를 arr와 같은 모양으로 만들어준다.
    stack = []
    visited = [[0] * N for _ in range(N)]


    ans = maze(arr)
    print(f'#{tc} {ans}')
