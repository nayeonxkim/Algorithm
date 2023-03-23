'''

가로 n
세로 n
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1

---
for i in range(N):
    for j in range(N):

width = [[0] * N] * N ]
arr[i][j] 가 1이면 blank += 1
0이면 blank = 0
해서 width[i][j]에 할당
[0 0 1 2 3]
[1 2 3 4 0]
[0 0 1 0 0]
[0 1 2 3 4]
[1 2 3 0 1]
-> 가로 최대가 3이면 point+=1
for i in range(N)
    max(arr[i]) == 3
---
height = [0] * N
arr[j][i] 가 1이면 blank += 1
0이면 blank = 0
해서 width[j][i]에 할당
[0 0 1 1 1]
[1 1 2 2 1]

-> 세로 최대가 3이면 point+=1
height_list = []
for i in range(N)
    for j in range(N)
        height_list.append(arr[j][i])
        if max(height_list) == 3
            point += 1
---
K_copy = K
for i
    for j
        K_copy = K_copy - arr[i][j]
    K_copy가 0이다 => point += 1

K_copy = K
for j
    for i
        K_copy = K_copy - arr[i][j]



'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [[] for i in range(N)]
    for i in range(N):
        arr_num = list(map(int, input().split()))
        arr[i] = arr_num

    print(arr)

