import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]
    row = 99
    for j in range(100):
        if arr[row][j] == 2:
            col = j

    while row > 0:
        if col-1 >= 0 and arr[row][col-1] == 1:
            arr[row][col] = 0
            col -= 1

        elif col+1 < 100 and arr[row][col+1] == 1:
            arr[row][col] = 0
            col += 1

        else:
            row -= 1

    print(f'#{tc} {col}')
