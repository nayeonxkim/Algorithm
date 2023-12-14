import sys
sys.stdin = open('input.txt')
from collections import deque

words = input()
nums = deque()
ops = deque()

for n in words:
    if n.isdecimal():
        nums.append(int(n))

    elif n == '+':
        n2, n1 = nums.pop(), nums.pop()
        nums.append(n1 + n2)

    elif n == '-':
        n2, n1 = nums.pop(), nums.pop()
        nums.append(n1 - n2)

    elif n == '*':
        n2, n1 = nums.pop(), nums.pop()
        nums.append(n1 * n2)

    elif n == '/':
        n2, n1 = nums.pop(), nums.pop()
        nums.append(n1 / n2)

print(*nums)