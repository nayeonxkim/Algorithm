import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

total_cnt = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            queue = [(i, j)]
            visited[i][j] = 1

            cnt = 1
            while queue:
                row, col = queue.pop(0)
                for k in range(4):
                    ni = row + di[k]
                    nj = col + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            queue.append((ni, nj))
                            cnt += 1

            total_cnt.append(cnt)

print(max(total_cnt))