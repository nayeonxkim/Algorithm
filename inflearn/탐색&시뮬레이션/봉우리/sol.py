import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
tot = 0
for i in range(N):
    for j in range(N):
        top = 1
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] >= arr[i][j]:
                    top = 0
                    break

        if top == 1:
            tot += 1

print(tot)
