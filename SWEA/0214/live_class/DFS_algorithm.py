import sys
sys.stdin = open('input.txt')

N, E = map(int, input().split())
data = list(map(int, input().split()))

arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(E):
    # data의 짝수 번째 요소는 행 번호, 홀수번째 요소는 열 번호가 된다.
    arr[data[i*2]][data[i*2+1]] = 1
    arr[data[i*2+1]][data[i*2]] = 1
    # 왕복 가능하기 때문에 행, 열 바꿔서도 1 입력

start = 1
stack = [start] # 출발하는 노드는 하나 넣어두고 시작
visited = [False] * (N+1)

while stack:
    start = stack.pop()
    # 이전에 방문한 적 없다면
    if not visited[start]:
        # 해당 지점을 방문표시하고
        visited[start] = True
        print(start, end = '-')
        for j in range(1, N + 1):
            # start에서 next로 이동가능하고, next에 방문한적 없다면
            if arr[start][j] == 1 and not visited[j]:
                stack.append(j)


for i in range(N+1):
    print(arr[i])
