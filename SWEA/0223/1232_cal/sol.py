import sys
sys.stdin = open('input.txt')



def inorder(node):
    global cal
    if node != 0:
        # 1. 왼쪽 자식노드
        inorder(left[node])

        # 2. 자기자신
        cal.append(tree[node])

        # 3. 오른쪽 자식노드
        inorder(right[node])


#
# def calculator(cal):
#     stack = []
#     numbers = []
#
#     for char in cal:
#         if char in '+-*/':
#             stack.append(char)
#
#     for i in range(N - 1, -1, -1):
#         if cal[i] not in '+-*/':
#             numbers.append(int(cal[i]))
#
#     while stack:
#         if stack and stack.pop(0) == '-':
#             n1 = numbers.pop()
#             n2 = numbers.pop()
#             numbers.append(n1 - n2)
#         elif stack and stack.pop(0) == '+':
#             n1 = numbers.pop()
#             n2 = numbers.pop()
#             numbers.append(n1 + n2)
#         elif stack and stack.pop(0) == '*':
#             n1 = numbers.pop()
#             n2 = numbers.pop()
#             numbers.append(n1 * n2)
#         elif stack and stack.pop(0) == '/':
#             n1 = numbers.pop()
#             n2 = numbers.pop()
#             numbers.append(n1 / n2)
#
#     return numbers

for tc in range(1, 10):
    N = int(input())

    tree = [''] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        data = list(input().split())

        idx = int(data[0])

        if data[1].isdecimal():
            tree[idx] = data[1]
        else:
            tree[idx] = data[1]

        if len(data) == 4:
            left[idx] = int(data[2])
            right[idx] = int(data[3])
        elif len(data) == 3:
            left[idx] = int(data[2])


    cal = []
    inorder(1)
    print(cal)

    # print(calculator(cal))

    stack = []
    numbers = []

    for char in cal:
        if char in '+-*/':
            stack.append(char)

    for i in range(N - 1, -1, -1):
        if cal[i] not in '+-*/':
            numbers.append(int(cal[i]))

    while stack:
        # if len(numbers) == 1:
        #     break

        if stack[0] == '-':
            n1 = numbers.pop()
            n2 = numbers.pop()
            numbers.append(n1 - n2)
        elif stack[0]  == '+':
            n1 = numbers.pop()
            n2 = numbers.pop()
            numbers.append(n1 + n2)
        elif stack[0]  == '*':
            n1 = numbers.pop()
            n2 = numbers.pop()
            numbers.append(n1 * n2)
        else:
            n1 = numbers.pop()
            n2 = numbers.pop()
            numbers.append(n1 / n2)
        stack.pop(0)

    print(stack)
    print(numbers)
    print()




