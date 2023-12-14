import sys
sys.stdin = open('input.txt')
from collections import deque

num, m = input().split()
num = list(map(int, num))
m = int(m)

stack = deque()
cnt = 0
for n in num:
    while stack and stack[-1] < n and cnt < m:
            stack.pop()
            cnt += 1

    stack.append(n)

while cnt < m:
    stack.pop()
    cnt += 1
print(''.join(str(x) for x in stack))
