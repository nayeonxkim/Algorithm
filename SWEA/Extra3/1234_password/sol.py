import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, numbers = input().split()

    stack = []
    for num in numbers:

        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)

    ans = ''
    for num in stack:
        ans += num

    print(f'#{tc} {int(ans)}')

