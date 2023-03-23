import sys
sys.stdin = open('input.txt')

def check(arr):

    for lst in arr:
        point = 0
        for char in lst:
            if char == 'o':
                point += 1
                if point == 5:
                    return 1
            else:
                point = 0
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 가로
    ans1 = check(arr)

    # 세로
    arr_t = list(zip(*arr))
    ans2 = check(arr_t)

    # 왼->오 대각선
    point = ans3 = 0
    for i in range(N - 1):
        for j in range(N - 1):
             while arr[i][j] == 'o':
                    point += 1
                    if 0 <= i < N - 1 and 0 <= j < N - 1:
                        i += 1
                        j += 1

                    if point == 5:
                        ans3 = 1
                        break



    # 오->왼 대각선
    point = ans4 = 0
    for i in range(N - 1):
        for j in range(N-1, 0, -1):
            row, col = i, j
            while 0 <= row < N and 0 <= col < N:
                if arr[row][col] == 'o':
                    point += 1
                    if point == 5:
                        ans4 = 1
                        break
                row += 1
                col -= 1


    if ans1 or ans2 or ans3 or ans4:
        ans = 'YES'
    else:
        ans = 'NO'

    print(f'#{tc} {ans}')