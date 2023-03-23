import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')

    N = int(input())
    arr = [(list(map(int, input().split()))) for _ in range(N)]

    # 90도 회전
    arr_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[j][N-1-i] = arr[i][j]

    # 180도 회전
    arr_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_180[j][N - 1 - i] = arr_90[i][j]

    # 270도 회전
    arr_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_270[j][N - 1 - i] = arr_180[i][j]


    for i in range(N):
        # print(''.join(str(j) for j in arr_90[i]))
        print(''.join(map(str, arr_90[i])), ''.join(map(str, arr_180[i])), ''.join(map(str, arr_270[i])))