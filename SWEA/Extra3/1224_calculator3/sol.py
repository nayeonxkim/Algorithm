import sys
sys.stdin = open('input.txt')

def postfix(cal):
    stack = []
    new_cal = ''
    for char in cal:

        if char not in '*/+-()':
            new_cal += char

        elif char == '(':
            stack.append(char)

        elif char in '*/':
            while stack and stack[-1] in '*/':
                new_cal += stack.pop()
            stack.append(char)

        elif char in '+-':
            while stack and stack[-1] != '(':
                new_cal += stack.pop()
            stack.append(char)

        elif char == ')':
            while stack and stack[-1] != '(':
                new_cal += stack.pop()
            stack.pop()
            # 여는 괄호는 닫힌 괄호를 만나면 없애준다.

    return new_cal

def solve(new_cal):
    stack = []
    for char in new_cal:

        if char not in '*/+-':
            stack.append(char)

        elif char == '-':
            n2 = int(stack.pop())
            n1 = int(stack.pop())
            stack.append(n1 - n2)

        elif char == '+':
            n2 = int(stack.pop())
            n1 = int(stack.pop())
            stack.append(n1 + n2)

        elif char == '*':
            n2 = int(stack.pop())
            n1 = int(stack.pop())
            stack.append(n1 * n2)

        elif char == '/':
            n2 = int(stack.pop())
            n1 = int(stack.pop())
            stack.append(n1 / n2)

    return stack[-1]

for tc in range(1, 11):
    N = int(input())
    cal = list(input())

    new_cal = postfix(cal)
    ans = solve(new_cal)
    print(f'#{tc} {ans}')