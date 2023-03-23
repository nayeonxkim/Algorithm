import sys
sys.stdin = open('input.txt')

def BFS(arr):

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]
0
    queue = []
    visited = [[0] * N for _ in range(N)]

    cnt_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = 1

                cnt = 1
                while queue:

                    row, col = queue.pop(0)

                    for k in range(4):
                        ni = row + di[k]
                        nj = col + dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 1 and not visited[ni][nj]:
                                queue.append((ni, nj))
                                visited[ni][nj] = 1
                                cnt += 1

                cnt_lst.append(cnt)

    return cnt_lst

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]


ans = BFS(arr)
ans.sort()

print(len(ans))
for i in range(len(ans)):
    print(ans[i])