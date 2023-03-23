import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = list(range(M)) * M
    dj = sorted(di)

    max_res = 0
    for i in range(N):
        for j in range(N):
            res = 0
            for k in range(M*M):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    res += arr[ni][nj]
                if max_res < res:
                    max_res = res

    print(max_res)