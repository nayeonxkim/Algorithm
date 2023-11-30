import sys
sys.stdin = open('input.txt')

arr = [list(map(int, input().split())) for _ in range(7)]

# 1. 행
for i in range(3):
    for j in range(3):
        if arr[i][j:j+5] == arr[i][j:j+5:-1]:
            print(arr[i][j:j+5])

