import sys
sys.stdin = open('input.txt')

def BFS(row, col, N):
    visited = [[-1] * N for _ in range(N)]  # visited 생성

    queue = []  # 큐 생성
    queue.append((row, col))  # 시작점 인큐
    visited[row][col] = 0  # 시작점 방문 기록

    # 방향 제어
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 큐에 값이 있을 때까지 반복
    while queue:
        # 정점 꺼내
        row, col = queue.pop(0)

        if arr[row][col] == 3:
            return visited

        # 인접 노드들을 큐에 집어 넣고 방문기록 하기
        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != 1 and visited[ni][nj] == -1:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[row][col] + 1
                    if arr[ni][nj] == 3:
                        return visited[ni][nj] - 1


    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                row, col = i, j

    res = BFS(row, col, N)
    print(f'#{tc} {res}')
