import sys
sys.stdin = open('input.txt')

def backtrack(i, cost):

    global min_cost

    # 백트래킹 : 현재 비용이 최소 비용보다 이미 크다면 그만 조사하기
    if min_cost <= cost:
        return

    # 종료조건 : 모든 행 조사 끝나면 최소값 업뎃하고 함수 종료
    if i == N:
        min_cost = min(min_cost, cost)

    # 재귀 호출 : 방문한 열 체크 후 다음 행 조사, 다시 현재로 돌아오면 방문기록 취소
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                backtrack(i+1, cost + arr[i][j])
                visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N # 열 방문기록 리스트

    min_cost = 99 * 15
    # 첫 행과 비용
    backtrack(0, 0)
    print(f'#{tc} {min_cost}')