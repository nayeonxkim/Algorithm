import sys
sys.stdin = open('input.txt')

# 자신이 속한 집단의 대표원소 : parent를 구하는 함수
# 인덱스 = 값이 일치할때까지 계속 찾아감.
def find_set(x):
    # 1. 반복문
    while parent[x] != x:
        x = parent[x]
    return x

    # 2. 재귀
    if x == parent[x]:
        return x
    return find_set(parent[x])
def union(x, y):
    # parent[y의 부모] = x의 부모
    # parent[find_set(y)] = find_set(x)
    # print(parent, x, y)

    x = find_set(x)
    y = find_set(y)

    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y

    if rank[x] == rank[y]:
        rank[x] += 1

T = int(input())
for tc in range(1, T+1):
    # N = 전체 사람 수, M = 쪽지 수
    N, M = map(int, input().split())
    # 간선정보
    edge = list(map(int, input().split()))

    # make-set
    # 부모정보를 넣을 리스트 생성 : 일단은 자기자신을 부모로 둠.
    parent = list(range(N+1))

    # 자기자신X, 동일한 수준에서 시작
    rank = [0] * (N+1)

    # union

    for i in range(M):
        x, y = edge[i*2], edge[i*2+1]
        union(x, y)

    result = set()
    for i in range(1, N+1):
        result.add(find_set(i))
    print(f'#{tc} {len(result)}')