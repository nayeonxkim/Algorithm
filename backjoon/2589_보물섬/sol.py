import sys
sys.stdin = open('input.txt')
from collections import deque
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

print(arr)
minV = 50 * 50
def BFS(arr):
    global minV
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]


    visited = [[0] * C for _ in range(R)]
    queue = deque()

    # 시작점 찾기
    for i in range(R):
        for j in range(C):

            # 시작점에서
            if arr[i][j] == 'L' and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = 1
                cnt = 0


                while queue:
                    r, c = queue.popleft()

                    for k in range(4):
                        ni, nj = r + di[k], c + dj[k]
                        if 0 <= ni < R and 0 <= nj < C:
                            if not visited[ni][nj] and arr[ni][nj] == 'L':
                                queue.append((ni, nj))
                                visited[ni][nj] = 1
                                cnt += 1

                minV = min(minV, cnt)

BFS(arr)
print(minV)