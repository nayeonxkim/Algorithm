import sys
sys.stdin = open('input.txt')

# M이 가로, N이 세로
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    print(arr[i])
visited = [[0] * M for _ in range(N)]
print('==')
q_start = []
def BFS(arr):

    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]


    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                q_start.append((i, j))

    for _ in range(len(q_start)):
        queue = []
        queue.append(q_start.pop(0))

        while queue:
            r, c = queue.pop(0)

            for k in range(4):
                ni = r + di[k]
                nj = c + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if not arr[ni][nj] and not visited[ni][nj]:
                        visited[ni][nj] = visited[r][c] + 1
                        queue.append((ni, nj))

BFS(arr)

for i in range(N):
    print(visited[i])
# ans = max(max(visited)) -1
# for i in range(N):
#     for j in range(M):
#         if not arr[i][j] and not visited[i][j]:
#             ans = -1
#             break

print('==')
print(q_start)