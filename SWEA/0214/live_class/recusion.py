import sys
sys.stdin = open('input.txt')

N, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접행렬
arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(E):
    arr[data[i*2]][data[i*2+1]] = 1
    arr[data[i*2+1]][data[i*2]] = 1

def DFS(start):
    visited[start] = True
    print(start, visited)

    for next in range(1, N+1):
        if arr[start][next] == 1 and not visited[next]:
            DFS(next)
# 스택을 따로 만들지 않고 재귀함수의 호출을 스택처럼 사용
visited = [False] * (N+1)
DFS(1)