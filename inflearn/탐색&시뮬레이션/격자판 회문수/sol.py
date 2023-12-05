'''
0,0 -> 0,6
0,1 -> 1,6
0,2 -> 2,6
0,6 -> 6,6

1,0 -> 0,5
1,1 -> 1,5

i, j = j, 6-i

'''
import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# 1. 행
for i in range(7):
    for j in range(3):
        if arr[i][j:j+5] == list(reversed(arr[i][j:j+5])):
            cnt += 1

# 2. 열 우선 arr로 변경
new_arr = [[0]*7 for _ in range(7)]
for i in range(7):
    for j in range(7):
        new_arr[j][6-i] = arr[i][j]

# 2. 열
for i in range(7):
    for j in range(3):
        if new_arr[i][j:j+5] == list(reversed(new_arr[i][j:j+5])):
            cnt += 1

print(cnt)

