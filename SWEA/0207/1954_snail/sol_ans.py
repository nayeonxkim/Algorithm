import sys
sys.stdin = open('input.txt')


T = int(input()) # tc -> 2

for tc in range(1, T+1):
    N = int(input()) # n -> n*n 사각형

    # dx / dy 항상 고정
    dx = [0, 1, 0, -1] # 좌, 우
    dy = [1, 0, -1 ,0] # 상, 하

    # N*N 리스트생성
    snail = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 1 # 순서마다 cnt 올라가서 값 더함
    r, c = 0, 0 #방향제어 각각 dx/dy 제어 (현 위치)
    d = 0 # 방향 세부 제어

    for i in range(N):
        for j in range(N):
            snail[r][c] = cnt
            r += dx[d]
            c += dy[d]
            #범위 초과 or 이미 방문
            if not (0 <= r < N and 0 <= c < N) or snail[r][c] != 0:
                #뒤로 이동
                r -= dx[d]
                c -= dy[d]
                #회전
                d = (d+1) % 4
                #한칸 이동
                r += dx[d]
                c += dy[d]
            cnt +=1

    print(f'#{tc}')
    for i in range(N):
        print(*snail[i])