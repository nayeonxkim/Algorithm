'''
1. char == '>'
: 스택에 무조건 <있음
0번 부터 pop

2. 공백 & 스택에 <없음
stack.append(char)
: stack.pop()

3. < & 스택에 값이 있음
stack.pop()
stack.append(char)
'''


import sys
sys.stdin = open('input.txt')

sentence = sys.stdin.readline()

stack = []
ans = ''
for char in sentence:
    if char == '>':
        stack.append(char)
        while stack:
            ans += stack.pop(0)

    elif '<' not in stack and char == ' ':
        while stack:
            ans += stack.pop()
        ans += char

    elif char == '<' and stack:
        while stack:
            ans += stack.pop()
        stack.append(char)

    else:
        stack.append(char)

while stack:
    ans += stack.pop()
print(ans)