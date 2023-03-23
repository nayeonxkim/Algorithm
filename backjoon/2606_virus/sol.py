import sys
sys.stdin = open('input.txt')

N = int(input())
E = int(input())

arr = [[0] * (N+1) for _ in range(N+1)] # 0번 컴퓨터는 없으므로 0번 인덱스는 사용하지 않는다.

for _ in range(E):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

stack = [1]
visited = [0] * (N+1)
visited[1] = 1

cnt = 0
while stack:
    start = stack.pop()
    for j in range(1, N+1):
        if arr[start][j] == 1 and not visited[j]:
            stack.append(j)
            visited[j] = 1
            cnt += 1

print(cnt)