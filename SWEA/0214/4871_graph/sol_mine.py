import sys
sys.stdin = open('input.txt')

def DFS(start):
    # start 방문기록하고 시작
    visited[start] = 1
    stack = [start]

    # stack에 값이 있을 때까지만 반복
    while stack:
        # start지점을 stack의 마지막 요소로 업데이트
        start = stack.pop()

        # 만약 start 지점이 goal이면 1 반환 후 종료
        if start == goal:
            return 1

        # 갈 수 있는 인접노드 찾아서 방문하기
        for next in range(1, V+1):
            if arr[start][next] == 1 and not visited[next]:
                visited[next] = 1
                stack.append(next)
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        n1, n2 = map(int, input().split())
        arr[n1][n2] = 1

    start, goal = map(int, input().split())
    visited = [0] * (V+1)

    ans = DFS(start)
    print(f'#{tc} {ans}')
