import sys
sys.stdin = open('input.txt')
from collections import deque

S, E = map(int, input().split())

# 배열 & 큐 생성
visitied = [0] * (max(S, E) + 1)
queue = deque()

# 출발점 큐에 넣기
visitied[S] = 1
queue.append(S)

# BFS 탐색
while queue:
    now = queue.popleft()

    for m in [1, -1, 5]:
        next = now + m
        if 0 < next < len(visitied) and not visitied[next]:
            visitied[next] = visitied[now] + 1
            queue.append(next)

print(visitied[E] - 1)