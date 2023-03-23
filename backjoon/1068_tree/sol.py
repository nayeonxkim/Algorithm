import sys
sys.stdin = open('input.txt')

N = int(input())
parent = list(map(int, input().split()))
D = int(input())

# 내 밑에 연결된 노드가 있는지 확인하기
# : 스택에 푸쉬하여 나를 부모로 하는 노드들이 있는지 parent배열에서 확인한다.

# 노드 지우기
# : parent배열에서 지울 노드의 번호 = 해당 인덱스의 값을 -2로 바꾼다.


# 첫 노드 지우기
stack = [D]
parent[D] = -2

# 스택이 있는 동안
while stack:
    # 스택을 pop하여 idx에 할당한다.
    idx = stack.pop()

    # parent 배열을 처음부터 끝까지 순회하며 지울 노드를 부모로하는 리프 노드들이 있는 지 확인한다.
    for i in range(N):
        # parent배열의 값이 idx(지운 노드)와 일치하는 경우,
        # 지운 노드에 연결된 리프 노드라는 뜻이므로
        # 해당 노드번호를 스택에 푸쉬하고
        # 해당 노드는 없앤다. = 값을 -2로 바꾼다.
        if parent[i] == idx:
            stack.append(i)
            parent[i] = -2

ans = 0
# 전체 노드에 대하여
# parent배열에 해당 값이 존재하지 않으며 : 자신을 부모로 하는 노드가 없음 = 리프노드임
# parent배열의 해당 인덱스의 값이 -2가 아닌 경우 : 없어지지 않은 노드
for i in range(N):
    if i not in parent and parent[i] != -2:
        # ans에 +1
        ans += 1

print(ans)