'''

내 크기 baby = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] < baby:
            stack.append((i,j))




'''

import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    print(arr[i])

