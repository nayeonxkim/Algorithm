import sys
sys.stdin = open('input.txt')
from collections import deque
inp = input()

stack = deque()
cnt = 0
laser = False
for char in inp:
    # (인 경우
    if char == '(':
        stack.append(char)
        laser = True

    # )인 경우
    else:
        if laser:
            stack.pop()
            cnt += len(stack)

        else:
            stack.pop()
            cnt += 1
            
        laser = False

print(cnt)
