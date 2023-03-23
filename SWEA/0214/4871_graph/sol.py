import sys
sys.stdin = open('input.txt')

def DFS(start):
    # 첫 시작위치 방문표시하고 시작
    visited[start] = True
    stack = [start]

    while stack:
        start = stack.pop()
        if start == G:
            return 1
        for next in range(1, N+1):
            if arr[start][next] and not visited[next]:
                visited[next] = True
                stack.append(next)
    return 0

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(E):
        r, c = map(int, input().split())
        arr[r][c] = 1

    S, G = map(int, input().split())

    visited = [False] * (N+1)
    print(DFS(S))




