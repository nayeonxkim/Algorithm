import sys
sys.stdin = open('input.txt')

def DFS(v):
    if v == N+1:
        for i in range(1, N+1):
            if visited[i]:
                print(i, end=' ')
        print()
    else:
        visited[v] = 1
        DFS(v+1)
        visited[v] = 0
        DFS(v+1)


N = int(input())
visited = [0] * (N+1)
DFS(1)
