import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


stack = []
cnt_lst = []
Flag = True
while Flag:
    if arr == visited:
        Flag = False

    for i in range(N):
        for j in range(N):
            if arr[i][j] and not visited[i][j]:
                stack.append((i, j))
                visited[i][j] = 1
                break
            break
    # 단지 별
    cnt = 1
    while stack:
        row, col = stack.pop()

        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] and not visited[ni][nj]:
                    stack.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt += 1

    cnt_lst.append(cnt)



print(len(cnt_lst))
for n in sorted(cnt_lst):
    print(n)