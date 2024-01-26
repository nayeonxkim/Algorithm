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
        # 다음 칸이 범위 내에 있고 방문한적 없으면 -> 현재 위치 + 1로 방문표시
        if 0 < next < len(visitied) and not visitied[next]:
            visitied[next] = visitied[now] + 1
            queue.append(next)

# 도착점에 이미 방문하면 더이상 표시 X -> 가장 작은 수가 표시 됨
print(visitied[E] - 1)