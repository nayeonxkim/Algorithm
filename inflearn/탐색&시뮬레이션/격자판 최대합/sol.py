import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max = 0
# 1. 행의 합
for i in range(N):
    row = 0
    for j in range(N):
        row += arr[i][j]

    if row > max:
        max = row

# 2. 열의 합
for j in range(N):
    col = 0
    for i in range(N):
        col += arr[i][j]

    if col > max:
        max = col

#  3. 대각선의 합
right = left = 0
for i in range(N):
    right += arr[i][i]
    left += arr[i][N-1-i]

if right > max:
    max = right

if left > max:
    max = left

print(max)
