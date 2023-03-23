import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    word = input()
    stack = []
    for char in word:
        if char == '(':
            stack.append(char)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else: # 앞글자가 )이거나 스택이 빈경우
                stack.append(char)

    if stack:
        print('NO')
    else:
        print('YES')
