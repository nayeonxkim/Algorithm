import sys
sys.stdin = open('input.txt')

def BFS(arr):
    visited = [[0] * 16 for _ in range(16)]

    # 시작점 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                queue = [(i, j)]
                visited[i][j] = 1
                break

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 시작점
    while queue:
        row, col = queue.pop(0)

        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if 0 <= ni < 16 and 0 <= nj < 16:
                if arr[ni][nj] != 1 and not visited[ni][nj]:
                    queue.append((ni, nj))
                    visited[ni][nj] = 1
                    if arr[ni][nj] == 3:
                        return 1
    return 0


# 0=길, 1=벽, 2=출발점, 3=도착점
for _ in range(10):
    tc = int(input())

    arr = [list(map(int, input())) for _ in range(16)]

    print(f'#{tc} {BFS(arr)}')


