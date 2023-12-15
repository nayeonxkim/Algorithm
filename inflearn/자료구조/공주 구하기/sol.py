import sys
sys.stdin = open('input.txt')
from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))

while len(queue) >= 2:
    queue.rotate(-(K-1))
    queue.popleft()
print(*queue)