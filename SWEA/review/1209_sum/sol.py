import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행의 합
    ans_row = [0] * 100
    for i in range(100):
        for j in range(100):
            ans_row[i] += arr[i][j]

    # 열의 합
    arr_t = list(zip(*arr))
    ans_col = [0] * 100
    for i in range(100):
        for j in range(100):
            ans_col[i] += arr_t[i][j]

    # 대각선의 합
    dia_sum = [0] * 2
    for i in range(100):
        dia_sum[0] += arr[i][i]
        dia_sum[1] += arr[i][99-i]

    ans = max(max(ans_row), max(ans_col), max(dia_sum))
    print(f'#{tc} {ans}')
