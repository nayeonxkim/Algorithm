import sys
sys.stdin = open('input.txt')

def BFS(arr):

    visited = [[0] * 100 for _ in range(100)]

    # 시작점 찾기
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                queue = [(i, j)]
                visited[i][j] = 1
                break

    # 4방향 제어
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    while queue:
        # 시작점을 현재 위치로 설정하기
        row, col = queue.pop(0)

        # 현재 위치에서 4방향 탐색하여 갈 수 있는 곳 인큐
        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if 0 <= ni < 100 and 0 <= nj < 100:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = 1

                    if arr[ni][nj] == 3:
                        return 1
    return 0


for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(100)]

    print(f'#{tc} {BFS(arr)}')