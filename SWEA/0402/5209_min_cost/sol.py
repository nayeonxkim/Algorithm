import sys
sys.stdin = open('input.txt')

def backtrack(i, N, cost):
    global minC

    if cost >= minC:
        return

    if i == N:
        minC = min(minC, cost)
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            backtrack(i+1, N, cost + arr[i][j])
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minC = 15 * 99
    # 이미 생산한 공장 표시
    visited = [0] * N
    backtrack(0, N, 0)
    print(f'#{tc} {minC}')