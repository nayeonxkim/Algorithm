import sys
sys.stdin = open('input.txt')
from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque([x for x in enumerate(arr)])

cnt = 0
while queue:
    maxV = max(queue, key=lambda x:x[1])

    if queue[0] == maxV:
        now = queue.popleft()
        cnt += 1
        if now[0] == M:
            print(cnt)

    else:
        queue.append(queue.popleft())

