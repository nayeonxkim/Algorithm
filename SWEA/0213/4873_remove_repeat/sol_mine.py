import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()

    stack = []

    for char in word:
        if not stack or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()

    print(f'{tc} {len(stack)}')