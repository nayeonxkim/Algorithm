'''
( -> 스택에 추가
) -> 짝이 맞는지 확인
'''

import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())


def check_char(value):

    stack = deque()

    for char in value:
        
        # (인 경우
        if char == '(':
            # 스택에 추가
            stack.append(char)
            
        # )인 경우
        else:
            # 스택에 값이 있다 = 짝이 맞다 -> pop해서 (없앰
            if stack:
                stack.pop()
            # 스택에 값이 없다 = 짝이 맞지 않다 -> NO 출력 후 종료
            else:
                print('NO')
                return
    
    # 모든 괄호 검사했는데 짝없는 (가 있는 경우 -> NO 출력
    if stack:
        print('NO')
    # 스택이 비었다면 (모든게 짝이 맞다면) -> YES 출력
    else:
        print('YES')



for i in range(N):
    value = input()
    check_char(value)

