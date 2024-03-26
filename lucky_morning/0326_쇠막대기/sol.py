import sys
sys.stdin = open('input.txt')
from collections import deque
inp = input()

'''
스택 = 
덩어리 =3 + 3 + 1 + 3 + 1 + 2 + 2+ 1 + 1
'''

cnt = 0
stack = deque()
laser = True

for char in inp:

    if char == '(':
        stack.append(char)
        laser = True

    else:
        if laser:
            stack.pop()
            cnt += len(stack)

        else:
            stack.pop()
            cnt += 1

        laser = False

print(cnt)