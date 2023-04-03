'''

1부터 7번까지의 노드가 있는 그래프
총 8개의 노드가 주어진다.

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''

def dfs1(i, k):
    # 방문한
    visited[i] = 1



V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjL = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1) # 무방향 그래프 일때만

print(adjL)