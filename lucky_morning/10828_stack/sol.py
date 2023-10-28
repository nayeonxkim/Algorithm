'''
시간 복잡도 N 
- 입력값을 for문으로 받든 다 받아서 리스트를 for문으로 순회하든 시간 복잡도는 똑같이 O(N)이다
- 즉, 로직상으로 더이상 줄일 수 없음
- 백준에서 input 받는 시간을 줄일 수 있는 readline 사용
- 굳이 시간 복잡도가 저렇게 빡빡할 이유가 업따;; 자바 기준인듯

[0 0 0 0 0 0 0 0 0]

'''

import sys
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
stack = deque([0]) * N

top = -1

for _ in range(N):
    value = input().strip()

    if 'push' in value:
        top += 1
        stack[top] = value[5:]

    elif 'pop' in value:
        if top != -1:
            print(stack[top])
            top -= 1
        else:
            print(top)

    elif 'size' in value:
        print(top + 1)

    elif 'empty' in value:
        if top != -1:
            print(0)
        else:
            print(1)

    else:
        if top != -1:
            print(stack[top])
        else:
            print(top)

