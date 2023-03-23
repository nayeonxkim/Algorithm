import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()
    res = 1
    stack = []
    for char in word:
        if char == '(' or char == '{':
            stack.append(char)
        else:
            if char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack:
                    res = 0
                    break
                elif stack[-1] != '(':
                    res = 0
                    break

            if char == '}':
                if not stack or stack[-1] != '{':
                    res = 0
                    break
                else:
                    stack.pop()
        # else:
        #     if char == ')' and stack and stack[-1] == '(':
        #         stack.pop()
        #     elif char == '}' and stack and stack[-1] == '{':
        #         stack.pop()
        #     else:
        #         res = 0
        #         break

    if stack:
        res = 0

    print(res)