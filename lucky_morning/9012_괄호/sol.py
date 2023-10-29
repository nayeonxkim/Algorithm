import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())

def check_char(value):

    stack = deque()

    for char in value:

        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                return

    if stack:
        print('NO')

    else:
        print('YES')



for i in range(N):
    value = input()
    check_char(value)

