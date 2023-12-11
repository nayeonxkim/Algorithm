from collections import deque
import sys
sys.stdin = open('input.txt')

# 1. 입력받은 그래프를 인접행렬로 생성
N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    i, v = map(int, input().split())
    arr[i].append(v)
    arr[v].append(i)

# 2. 인접행렬 오름차순 정렬
for n in arr:
    n.sort()


# 3. DFS 탐색
# 방문표시 및 정답배열 생성
visited = [0] * (N+1)
ans_dfs = []
def DFS(c):
    # 방문표시 및 ans에 추가
    visited[c] = 1
    ans_dfs.append(c)
    # DFS 탐색
    for n in arr[c]:
        if visited[n] == 0:
            DFS(n)

DFS(V)
print(*ans_dfs)

# 4. BFS 탐색
# 방문표시 및 정답배열 생성
visited = [0] * (N+1)
ans_bfs = []
def BFS(s):
    # 큐 생성
    queue = deque()
    # 첫 시작점 방문표시 및 큐에 추가
    queue.append(s)
    visited[s] = 1

    # BFS 탐색
    while queue:
        now = queue.popleft()
        ans_bfs.append(now)
        for next in arr[now]:
            if visited[next] == 0:
                visited[next] = 1
                queue.append(next)

BFS(V)
print(*ans_bfs)
