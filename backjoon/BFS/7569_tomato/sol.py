import sys
sys.stdin = open('input.txt')
from collections import deque

M, N, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N*H)]

# 2. BFS 탐색
def BFS(arr, N):

    di = [-1, 0, 1, 0, -N, N]
    dj = [0, 1, 0, -1, 0, 0]

    while queue:
        r, c = queue.popleft()
        for k in range(6):
            ni = r + di[k]
            nj = c + dj[k]
            if not (r + 1) % N and k == 2:
                pass
            elif not r % N and k == 0:
                pass
            elif 0 <= ni < N*H and 0 <= nj < M:
                if not arr[ni][nj]:
                    arr[ni][nj] = arr[r][c] + 1
                    queue.append((ni, nj))

# 3. 정답
def answer(arr):
    maxV = 0
    for i in range(N*H):
        for j in range(M):
            if not arr[i][j]:
                return -1
            if maxV <= arr[i][j]:
                maxV = arr[i][j]
    return maxV - 1

# 1. 모든 1의 위치를 찾아 인큐
queue = deque()
for i in range(N*H):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j))
BFS(arr, N)
ans = answer(arr)

print(ans)