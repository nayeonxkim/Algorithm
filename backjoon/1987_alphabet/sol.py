import sys
sys.stdin = open('input.txt')

def DFS(arr):

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    stack = [(0, 0)]
    visited = []


    while stack:

        row, col = stack.pop()
        visited.append(arr[row][col])

        for k in range(4):
            ni = row + di[k]
            nj = col + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] not in visited:
                    stack.append((ni, nj))


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

for i in range(R):
    print(arr[i])