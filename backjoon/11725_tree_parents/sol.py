import sys
sys.stdin = open('input.txt')

N = int(input())

left = [0] * (N+1)
right = [0] * (N+1)
parent = [0] * (N+1)

for _ in range(N-1):
    node1, node2 = map(int, input().split())

    if node2 == 1:
        p, c = node2, node1
    else:
        p, c = node1, node2

    if left[p]:
        right[p] = c
    else:
        left[p] = c
    parent[c] = p

print(left)
print(right)
print(parent)

for i in range(1, N+1):
    if i in left:
        print(left.index(i))
    elif i in right:
        print(right.index(i))