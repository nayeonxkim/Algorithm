import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cal = input().split()

    stack = []

    for char in cal:
        if char not in '+-*/.':
            stack.append(char)


        else:
            if stack:
                    n2 = int(stack.pop())
                    try:
                        n1 = int(stack.pop())
                        if char == '+':
                            stack.append(n1 + n2)
                            print(stack)

                        elif char == '-':
                            stack.append(n1 - n2)
                            print(stack)

                        elif char == '*':
                            stack.append(n1 * n2)
                            print(stack)
                        elif char == '/':
                            stack.append(n1 / n2)
                            print(stack)
                        elif char == '.':
                            ans = stack[-1]




    print(f'#{tc} {ans}')