import sys
sys.stdin = open('input.txt')
from sys import stdin as s
from collections import deque

m, n = map(int, s.readline().split())

board = [list(map(int, s.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()
## 처음에 토마토 위치를 저장해야함
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            dq.append((i, j))


def bfs():
    while dq:
        now = dq.popleft()
        for k in range(4):
            xx = now[0] + dx[k]
            yy = now[1] + dy[k]
            if 0 <= xx < n and 0 <= yy < m:
                if board[xx][yy] == 0:
                    board[xx][yy] = board[now[0]][now[1]] + 1  ## 최댓값이 익은 날짜일것
                    dq.append((xx, yy))


bfs()
res = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:  ## 다돌았는데 안익은게 있다면 -1
            print(-1)
            exit(0)
res = max(map(max, board))  ## 익은날짜들이 들어있는 배열중에서 최댓값 추출
print(res - 1)  ## 1로시작했으니 -1을 해야 지난 날짜