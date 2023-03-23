import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cal = input()

    # 연산자 입력 스택
    stack = []
    # 최종 결과값
    res = ''


    for char in cal:
        if char in '+-*()':
            # 우선순위에 맞추어 stack에 쌓기
            if char == '(':
                stack.append(char)
            elif char in '*/':
                while stack and stack[-1] in '*/':
                    res += stack.pop()
                stack.append(char)
            elif char in '+-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()

        # 피연산자면 바로 res에 넣기
        else:
            res += char

    while stack:
        res += stack.pop()
    print(res)