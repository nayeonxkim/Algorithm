import sys
sys.stdin = open('input.txt')

# 전위순회
def preorder(node):
    # 왼쪽 자식이 없으면 오른쪽 자식한테 가야함
    # 조건문 안달면 계속 preorder(0) 호출함
    if node != 0:
        # 1. 나부터
        print(node, end = ' ')

        # 2. 왼쪽 자식노드
        preorder(left[node])

        # 3. 오른쪽 자식노드
        preorder(right[node])

# 중위순회
def inorder(node):
    if node != 0:
        # 1. 왼쪽 자식노드
        inorder(left[node])

        # 2. 자기자신
        print(node, end = ' ')

        # 3. 오른쪽 자식노드
        inorder(right[node])


# 후위순회
def postorder(node):
    if node:
        # 1. 왼쪽자식
        postorder(left[node])

        # 2. 오른쪽 자식
        postorder(right[node])

        # 3. 자기자신
        print(node, end = ' ')

V =  int(input())
E = V - 1
edge = list(map(int, input().split()))

# 인덱스를 활용하기 위해 노드보다 1개 많게 parent 배열 생성
parent = [0] * (V+1)
left = [0] * (V+1)
right = [0] * (V+1)

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    # print(p, c)
    if left[p] == 0:    # 아직 왼쪽 자식이 없으면
        left[p] = c     # 해당 부모 인덱스에 자식 노드의 값을 넣는다.
    else:               # 왼쪽에 자식이 있으면 오른쪽에 자식노드를 넣는다.
        right[p] = c
    parent[c] = p       # 해당 자식 노드의 부모가 누구인지 기록해둔다.
    # 부모에게는 최대 2개의 자식, 자식에게는 1개의 부모노드만 존재할 수 있다.
    # print(left)
    # print(right)


# 루트 노드 찾기
root = 0
for i in range(1, V+1):
    # 모든 노드를 순회하면서 부모노드가 없으면
    # 해당 노드를 root 노드로 한다.
    if parent[i] == 0:
        root = i
        break
        # 앞에서 찾으면 굳이 끝까지 돌 필요가 없기 때문에 break해준다.

print(root)
# 이 문제에서는 1번이 루트 노드

preorder(root)
print()
inorder(root)
print()
postorder(root)