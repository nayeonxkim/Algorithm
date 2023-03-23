import sys
sys.stdin = open('input.txt')

def check(word):
    while stack:
        for char in word:
            if stack[-1] == '(':
                if char == ')':
                    stack.pop()
            if stack[-1] == '{':
                if char == '}':
                    stack.pop()
    return 1

T = int(input())
for tc in range(1, T+1):
    word = input()

    stack = []
    for char in word:
        if char == '(' or char == '{':
            stack.append(char)


    print(check(word))
    print(stack)
