import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(19)]

# 연속된 값이 5개가 있는지

# 가로세로
def line(arr, color):
    res = 0
    for i in range(19):
        point = 0
        for j in range(19):
            if arr[i][j] == color:
                point += 1
                if point == 5:
                    res = color

                elif point == 6:
                    res = 0
                    break
            else:
                point = 0
    return res

# 가로
ans1_b = line(arr, 1)
ans1_w = line(arr, 2)
# 세로
arr_t = list(zip(*arr))
ans2_b = line(arr_t, 1)
ans2_w = line(arr_t, 2)

print(ans1_b, ans1_w)
print(ans2_b, ans2_w)


# # 좌 -> 우 대각선
# def left_right(arr, color):
#     for i in range(19):
#         for j in range(19):
#             if arr[i][j] == color:
#                 point = 1
#                 while True:
#                     i += 1
#                     j += 1
#                     if arr[i][j] == color:
#                         point += 1
#                         if point == 5:
#                             res = color
#                         elif point == 6:
#                             res = 0
#                             break