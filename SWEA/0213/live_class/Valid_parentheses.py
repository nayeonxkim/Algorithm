import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    bracket = input()
    # 괄호짝이 맞으면 1, 안맞으면 -1
    # 여는 괄호들만 스택에 담자
    stack = []
    res = 1
    for char in bracket:
        if char == '(':
            stack.append(char)
        else:
            if stack:
            # 여는 괄호가 아니면 : 닫는 괄호면 넣어둔 여는 괄호를 하나 뺀다.
                stack.pop()
            else:
                res = -1
                break

    # break를 당한 적이 없다면 : 반복문 밖에서 else!
    # 조사를 다 끝냈는데, stack에 값이 있으면 이것도 실패.
    else:
        if stack:
            res = -1

    print(f'#{tc} {res}')