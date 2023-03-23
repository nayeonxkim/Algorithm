N = 5
arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]


for i in range(5):
    print(arr[i])
# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(N-1):
    for j in range(N-1):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                print(arr[ni][nj])