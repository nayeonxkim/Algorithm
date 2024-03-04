import sys
sys.stdin = open('input.txt')
from collections import deque

N, M = map(int, input().split())
queue = deque(enumerate(map(int, input().split())))

cnt = 0
while queue:
    now = queue[0][1]
    for i in range(1, len(queue)):
        if queue[i][1] > now:
            queue.append(queue.popleft())
            break
    else:
        pop = queue.popleft()
        cnt += 1
        if pop[0] == M:
            print(cnt)