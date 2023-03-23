import sys
sys.stdin = open('input.txt')

T = int(input())

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]



for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))
        print(arr[i].count(1))


    # row = col = 0
    #
    # cnt = 0 # 유적의 길이
    # all_cnt = []
    # for i in range(N-1):
    #     for j in range(M-1):
    #         for k in range(4):
    #             ni = row + di[k]
    #             nj = col + dj[k]
    #             if 0 <= ni < N and 0 <= nj < M:
    #                 while arr[ni][nj] == 1:
    #                     arr[ni][nj] = 0
    #                     for i in range(N):
    #                         print(arr[i])
    #                     row, col = ni, nj
    #                     cnt += 1
    #
    #                     print(row, col)
    #                     print(cnt)
    #
