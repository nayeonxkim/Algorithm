import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(19)]
ans_row = ans_col = 0

# 가로세로
def line(arr):
    global ans_row
    global ans_col

    res = 0
    black = white = 0
    for i in range(19):
        for j in range(19):
            if arr[i][j] == 1:
                black += 1
                white = 0
                if black == 5:
                    res = 1
                    ans_row, ans_col = i, j-4
                elif black >= 6:
                    res = 0
                    return res
            elif arr[i][j] == 2:
                white += 1
                black = 0
                if white == 5:
                    res = 2
                elif white >= 6:
                    res = 0
                    return res
            else:
                black = white = 0
    return res

ans1 = line(arr)
arr_t = list(zip(*arr))
ans2 = line(arr_t)
if ans2:
    ans_row, ans_col = ans_col, ans_row

def left_right(arr, color):
    global ans_row
    global ans_col
    res = 0

    for i in range(19):
        for j in range(19):
            point = 0
            row, col = i, j
            if arr[row][col] == color:
                while arr[row][col] == color:
                    point += 1
                    if point == 5:
                        res = color
                        ans_row, ans_col = i, j
                    elif point >= 6:
                        res = 0
                        break
                    row += 1
                    col += 1
                    if row >= 19 or col >= 19:
                        break
                else:
                    point = 0
    return res

ans3_black = left_right(arr, 1)
ans3_white = left_right(arr, 2)

def right_left(arr, color):
    global ans_row
    global ans_col

    res = 0
    for i in range(19):
        for j in range(19):
            point = 0
            row, col = i, j
            if arr[row][col] == color:
                while arr[row][col] == color:
                    point += 1
                    if point == 5:
                        res = color
                        ans_row, ans_col = row, col
                    elif point >= 6:
                        res = 0
                        return res
                    row += 1
                    col -= 1
                    if row >= 19 or col < 0:
                        return res
                else:
                    point = 0
    return res
ans4_black = right_left(arr, 1)
ans4_white = right_left(arr, 2)
print(ans4_black)
ans = max([ans1, ans2, ans3_black, ans3_white, ans4_black, ans4_white])
# print(ans)
# if ans:
#     print(ans_row+1, ans_col+1)

