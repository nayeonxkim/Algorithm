'''
위쪽으로 쭉 쌓여있고 아래꺼도 싹다 빼서 위로 올리고 제일 앞에 꺼 뺴는거
'''

import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque(range(1, N + 1))
output = deque()

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    output.append(queue.popleft())


print("<" + ", ".join(map(str, output)) + ">")