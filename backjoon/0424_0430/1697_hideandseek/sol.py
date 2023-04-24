import sys
sys.stdin = open('input.txt')
from collections import deque

N, K = map(int, input().split())

def BFS(N, K):

    visited = [-1] * 100001
    queue = deque()

    visited[N] = 0
    queue.append(N)

    while queue:

        X = queue.popleft()

        if X == K:
            return visited[X]

        d = [X, -1, 1]

        for k in range(3):
            X_n = X + d[k]
            if 0 <= X_n <= 100000 and visited[X_n] == -1:
                visited[X_n] = visited[X] + 1
                queue.append(X_n)

ans = BFS(N, K)
print(ans)