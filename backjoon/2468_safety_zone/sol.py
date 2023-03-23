import sys
sys.stdin = open('input.txt')

def check(safe_zone):

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    stack = []

    Flag = True
    res = 0
    while Flag:

        if safe_zone == visited:
            Flag = False

        for i in range(N):
            for j in range(N):

                if safe_zone[i][j] and not visited[i][j]:
                    stack.append((i, j))
                    visited[i][j] = 1
                    res += 1

                    while stack:
                        row, col = stack.pop()

                        for k in range(4):
                            ni = row + di[k]
                            nj = col + dj[k]
                            if 0 <= ni < N and 0 <= nj < N:
                                if safe_zone[ni][nj] and not visited[ni][nj]:
                                    stack.append((ni, nj))
                                    visited[ni][nj] = 1

    return res



N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

max_ans = 0
for rain in range(max(max(arr))):
    cnt = 0
    safe_zone = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > rain:
                safe_zone[i][j] = 1

    ans = check(safe_zone)
    if max_ans < ans:
        max_ans = ans

print(max_ans)

