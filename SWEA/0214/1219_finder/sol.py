import sys
sys.stdin = open('input.txt')

# DFS 함수 정의
def DFS(start):
    # 첫 출발 지점에서 시작
    # = visited와 stack에 start 방문 기록하고 시작
    # 방문 기록 : visited의 해당 인덱스 1로 업데이트, stack에 push
    visited[start] = 1
    stack = [start]

    # stack에 값이 존재한다면 계속 반복
    while stack:
        # stack의 마지막 값으로 start 업데이트
        start = stack.pop()

        # 갈 수 있는 길 모아두는 곳

        # start 지점이 99(도착지점)와 같다면 1 반환 및 종료
        if start == goal:
            return 1

        # 다음 0부터 99까지 이동할 노드 찾음
        for next in range(100):
            # start에서 next 노드까지 길이 있고, next 노드에 방문한 적 없다면
            if arr[start][next] == 1 and not visited[next]:
                # 해당 next 노드 방문 기록
                visited[next] = 1
                stack.append(next)
    # 99까지 가지 못해서서
    return 0

for _ in range(10):
    tc, E = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[0] * 100 for _ in range(100)]

    # 짝수 인덱스 0, 2, 4, ...는 행
    # 홀수 인덱스 1, 3, 5, ...는 열
    for i in range(E):
        arr[lst[i*2]][lst[i*2+1]] = 1

    start, goal = 0, 99

    visited = [0] * 100
    ans = DFS(start)
    print(f'#{tc} {ans}')
