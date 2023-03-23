import sys
sys.stdin = open('input.txt')



N = int(input())

stack = []

for _ in range(N):
    cmd = input()

    if 'push' in cmd:
        stack.append(cmd[5:])

    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif cmd == 'pop':
        if stack:
            print(stack[-1])
            stack = stack[:-1]
        else:
            print(-1)
