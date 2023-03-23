import sys
sys.stdin = open('input.txt')

N = int(input())

tree = ['.'] * (N+1)
left = ['.'] * (N+1)
right = ['.'] * (N+1)

for i in range(1, N+1):
   tree[i], left[i], right[i] = input().split()

# 전위순회 : 나 왼 오
def preorder(node):

    if tree[node] != '.':
        print(tree[node], end = '')
        preorder(tree.index(left[node]))
        preorder(tree.index(right[node]))

# 중위순회 : 왼 나 오
def inorder(node):

    if tree[node] != '.':
        inorder(tree.index(left[node]))
        print(tree[node], end='')
        inorder(tree.index(right[node]))

# 중위순회 : 왼 나 오
def postorder(node):

    if tree[node] != '.':
        postorder(tree.index(left[node]))
        postorder(tree.index(right[node]))
        print(tree[node], end='')

preorder(1)
print()
inorder(1)
print()
postorder(1)