import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(arr):

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            ni = r + di[k]
            nj = c + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if not arr[ni][nj]:
                    arr[ni][nj] = arr[r][c] + 1
                    queue.append((ni, nj))

def answer(arr):
    maxV = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
            if maxV <= arr[i][j]:
                maxV = arr[i][j]

    return maxV - 1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j))


BFS(arr)
ans = answer(arr)
print(ans)

