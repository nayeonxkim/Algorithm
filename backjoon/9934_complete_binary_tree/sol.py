def order(node):

    if node != 0:
        order(left(node))

        print(node, end = ' ')

        order(right(node))


K = int(input())
for _ in range