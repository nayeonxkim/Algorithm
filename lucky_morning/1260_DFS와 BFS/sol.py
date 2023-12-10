from collections import deque
import sys
sys.stdin = open('input.txt')

# 1. 입력받기, 그래프 -> 2차원 배열
N, M, V = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i][j] = 1
    arr[j][i] = 1


# 2. DFS 탐색
def DFS(arr, V):
    visited = [0] * (N+1)
    # 첫 출발점 담음
    queue = deque()
    queue.append(V)
    ans = [V]
    visited[V] = 1

    while queue:
        now = queue.pop()
        for j in range(N+1):
            if visited[j] == 0 and arr[now][j] == 1:
                queue.append(j)
                visited[j] = 1
                ans.append(j)
    print(ans)

DFS(arr, V)

