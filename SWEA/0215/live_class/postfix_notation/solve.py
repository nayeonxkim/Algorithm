import sys
sys.stdin = open('input_cal.txt')

T = int(input())
for tc in range(1, T+1):
    cal = input()

    # 피연산자를 쌓을 스택 생성
    stack = []
    res = 0
    for char in cal:
        if char not in '+-*/':
            stack.append(char)
        else:
            n2 = int(stack.pop())
            n1 = int(stack.pop())
            if char == '+':
                stack.append(n1 + n2)

            elif char == '-':
                stack.append(n1 - n2)
            elif char == '*':
                stack.append(n1 * n2)
            elif char == '/':
                stack.append(n1 / n2)
    print(stack)