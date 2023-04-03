'''

1부터 7번까지의 노드가 있는 그래프
총 8개의 노드가 주어진다.

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''
# i = 출발노드, V = 노드의 개수
def dfs1(i, V):
    # 방문한 노드에 방문표시
    visited[i] = 1
    # 방문한 노드 출력
    print(i)
    for w in adjL[i]:
        # v와 연결되어있고, 방문한 적이 없는 노드라면,
        if visited[w] == 0:
            dfs1(w, V)

def dfs2(i, V):
    if not visited[i]:
        print(i)
        visited[i] = 1
    stack = []
    visited = [0] * (V+1)
    visited[i] = 1
    s = i
    while True:
        print(s)
        for w in adjL[s]:
            if not visited[w]:
                stack.append(w)
                s = w

        # 더이상 갈 수 있는 정점이 없으면, 스택에서 새로운 출발점을 꺼낸다.
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return





V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjL = [[] for _ in range(V+1)]

# 방문리스트
visited = [0] * (V+1)

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1) # 무방향 그래프 일때만
#
# dfs1(1, V)
dfs2(1, V)