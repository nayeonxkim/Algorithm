''''

i -> i+1
 슌서대로X
트리, 그래프

'''

import sys
sys.stdin = open('input.txt')

def backtrack(i, N, battery, cnt):
    global minV
    if minV <= battery:
        return

    if cnt == N-1:
        minV = min(minV, battery+arr[i][0])
        return

    for j in range(1, N):
        if not visited[j]:
            visited[j] = 1
            backtrack(j, N, battery + arr[i][j], cnt + 1)
            visited[j] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minV = 1000

    backtrack(0, N, 0, 0)

    print(f'#{tc} {minV}')