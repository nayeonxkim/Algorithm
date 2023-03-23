import sys
sys.stdin = open('input.txt')

# 후위표기법 함수
def postfix(cal):
    stack = []
    new_cal = ''

    for char in cal:
        if char not in '+*':
            new_cal += char

        elif char == '+':
            while stack:
                new_cal += stack.pop()
            stack.append(char)
        elif char == '*':
            while stack and stack[-1] == '*':
                new_cal += stack.pop()
            stack.append(char)

    while stack:
        new_cal += stack.pop()

    return new_cal

# 후위표기식을 계산하는 함수
def calculator(new_cal):
    stack = []
    res = 0

    for char in new_cal:
        if char not in '+*':
            stack.append(char)
        else:
            if stack:
                n2 = int(stack.pop())
                n1 = int(stack.pop())

                if char == '+':
                    stack.append(n1+n2)
                else:
                    stack.append(n1*n2)

    return stack[-1]

for tc in range(1, 11):
    N = int(input())
    cal = input()

    ans = calculator((postfix(cal)))
    print(f'#{tc} {ans}')

