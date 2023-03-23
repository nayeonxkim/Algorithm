import sys
sys.stdin = open('input.txt')


# 몇번만에 도착했는지 -> count가 아니라 visited의 값을 누적하여 구한다.
def BFS(arr):
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    queue = [(0, 0)]
    visited = [[0] * M for _ in range(N)]

    while queue:

        row, col = queue.pop(0)
        visited[0][0] = 1

        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] and not visited[ni][nj]:
                    queue.append((ni, nj))
                    visited[ni][nj] = visited[row][col] + 1

    return visited[N-1][M-1]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
ans = BFS(arr)
print(ans)

