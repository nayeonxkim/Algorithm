import sys
sys.stdin = open('input.txt')

def backtrack(i, N, SUM):
    global minS

    if minS <= SUM:
        return

    if i == N:
        minS = min(minS, SUM)
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            backtrack(i+1, N, SUM+arr[i][j])
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minS = 100
    visited = [0] * N
    backtrack(0, N, 0)
    print(f'#{tc} {minS}')