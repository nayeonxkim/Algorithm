import sys
sys.stdin = open('input.txt')

cal = input()

ans = ''
stack = []

for char in cal:
    if char not in '*/+-()':
        ans += char

    elif char in '*/':
        while stack and stack[-1] in '*/':
            ans += stack.pop()
        stack.append(char)

    elif char in '+-':
        while stack and stack[-1] in '*/-+':
            ans += stack.pop()
        stack.append(char)

    elif char == '(':
        stack.append(char)

    else:
        while stack[-1] != '(':
            ans += stack.pop()
        if stack[-1] == '(':
            stack.pop()

while stack:
    ans += stack.pop()
print(ans)
