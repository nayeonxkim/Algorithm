import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [[0] * N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
arr[r2][c2] = 1

queue = [(r1, c1)]
visited = [[0] * N for _ in range(N)]
visited[r1][c1] = 1

def BFS(queue):

    di = [-2, -2, 0, 0, 2, 2]
    dj = [-1, 1, -2, 2, -1, 1]

    while queue:
        row, col = queue.pop(0)

        for k in range(6):
            ni = row + di[k]
            nj = col + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[row][col] + 1
                    queue.append((ni, nj))

BFS(queue)
ans = visited[r2][c2]
print(ans-1)