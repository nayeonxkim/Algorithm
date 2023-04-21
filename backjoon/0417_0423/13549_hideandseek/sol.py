'''

1. queue에 갈 수 있는 위치
2. 방문배열 : 현재 위치에서 -1, 1, *2한 위치가 방문한 적이 없고
갈 수 있는 위치면
- 현재 위치 + 걸린 시간
- 해당 위치를 큐에 추가하여 다음 출발위치로 한다.
3. K에 도착하면 방문배열 값 출력

'''

import sys
sys.stdin = open('input.txt')
from collections import deque

N, K = map(int, input().split())

def BFS(N, K):

    queue = deque()
    visited = [-1] * 100001

    queue.append(N)
    # 첫 방문 표시할 때 0해야하니까
    visited[N] = 0

    while queue:
        X = queue.popleft()

        if X == K:
            return visited[X]

        d = [X, -1, 1]

        for k in range(3):
            X_n = X + d[k]
            if 0 <= X_n <= 100000 and visited[X_n] == -1:
                if k != 0:
                    visited[X_n] = visited[X] + 1
                queue.append(X_n)

ans = BFS(N, K)
print(ans)