import sys
sys.stdin = open('input.txt')

def DFS(arr, w, h):

    global cnt

    stack = []
    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visited[i][j]:
                visited[i][j] = 1
                cnt += 1
                stack.append((i, j))

                while stack:
                    r, c = stack.pop()
                    for k in range(8):
                        ni = r + di[k]
                        nj = c + dj[k]
                        if 0 <= ni < h and 0 <= nj < w:
                            if arr[ni][nj] and not visited[ni][nj]:
                                visited[ni][nj] = 1
                                stack.append((ni, nj))


while True:

    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    DFS(arr, w, h)
    print(cnt)
