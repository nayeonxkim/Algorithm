import sys
sys.stdin = open('input.txt')
from collections import deque

words = input()
stack = deque()
ans = ''

for char in words:
    # 1. 숫자라면
    if char.isdecimal():
        ans += char
    # 2. 연산자라면
    else:
        if not stack:
            stack.append(char)

        elif char == ')':
            while stack:
                ans += stack.pop()
                if stack[-1] == '(':
                    stack.pop()
                    break

        elif char in '+-':
            while stack and stack[-1] in '+-*/':
                ans += stack.pop()
            stack.append(char)

        elif char in '*/':
            while stack and stack[-1] in '*/':
                ans += stack.pop()
            stack.append(char)

        elif char == '(':
            stack.append(char)


while stack:
    ans += stack.pop()

print(ans)