from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

cnt_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            cnt = 1
            arr[i][j] = 0

            queue = deque()
            queue.append((i, j))

            while queue:
                r, c = queue.pop()
                for k in range(4):
                    ni, nj = r + di[k], c + dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj]:
                            cnt += 1
                            arr[ni][nj] = 0
                            queue.append((ni, nj))

            cnt_lst.append(cnt)

cnt_lst.sort()
print(len(cnt_lst))
for cnt in cnt_lst:
    print(cnt)