import sys
sys.stdin = open('input.txt')

def backtracking(i, tmp):

    global maxV

    # 가지치기
    if tmp <= maxV:
        return

    # 종료조건
    if i == N:
        maxV = max(maxV, tmp)
        return

    else:
        for j in range(N):
            if not visited[j]:
                # 방문표시 후
                visited[j] = 1
                # 다음 행 조사
                backtracking(i+1, tmp * arr[i][j] / 100)
                # 방문표시 초기화
                visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 해당 열을 방문한 적 있는지 표시할 1차원 배열
    visited = [0]*N
    maxV = 0
    # 0행부터 조사, 곱해줘야하니까 첫 확률은 1
    backtracking(0, 1)
    print(f'#{tc} {maxV*100:0.6f}')
