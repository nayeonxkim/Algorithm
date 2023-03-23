import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행의 합
    sum_row = [0] * 100
    for i in range(100):
        sum_row[i] = sum(arr[i])

    # 열의 합
    sum_col = [0] * 100
    for i in range(100):
        for j in range(100):
            if i > j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(100):
        sum_col[i] = sum(arr[i])

    # 대각선의 합
    dia_sum = 0
    for i in range(100):
        dia_sum += arr[i][j]

    # 반대 대각선의 합
    dia_sum2 = 0
    for i in range(100):
        dia_sum2 += arr[99-i][i]

    ans = max(max(sum_row), max(sum_col), dia_sum, dia_sum2)

    print(f'#{tc} {ans}')
