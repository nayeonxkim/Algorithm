# [오른쪽, 아래, 왼쪽, 위쪽]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 3 * 3 배열
N =3

for i in range(N):
    for j in range(N):
        for k in range(4):
            ni, nj =  i + di[k], j + dj[k]
            # 이동했는데 -1이 나오면 안됨. : 배열 밖을 벗어나면 안됨.
            if (0 <= ni < N) and (0 <= nj < N):
                print(i, j, ni, nj)
print('===============================================')

# for문 다르게 쓰기
for i in range(N):
    for j in range(N):
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj =  i + di, j + dj
            # 이동했는데 -1이 나오면 안됨. : 배열 밖을 벗어나면 안됨.
            if (0 <= ni < N) and (0 <= nj < N):
                print(i, j, ni, nj)
print('===============================================')
# 대각선 이동
for i in range(N):
    for j in range(N):
        for di, dj in [[1,1], [1,-1], [-1,-1], [-1,1]]:
            ni, nj =  i + di, j + dj
            # 이동했는데 -1이 나오면 안됨. : 배열 밖을 벗어나면 안됨.
            if (0 <= ni < N) and (0 <= nj < N):
                print(i, j, ni, nj)
print('===============================================')
# 좌우로 여러칸 이동
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 3 * 3 배열
N =3
# 세칸씩
P = 3
for i in range(N):
    for j in range(N):
        for k in range(4):
            for l in range(1, P+1):
                ni = i + di[k] * l
                nj = j + dj[k] * l
            # 이동했는데 -1이 나오면 안됨. : 배열 밖을 벗어나면 안됨.
                if (0 <= ni < N) and (0 <= nj < N):
                    print(i, j, ni, nj)


# 전치 행렬
arr = [[1,2,3], [4,5,6], [7,8,9]]

for row in range(3):
    for col in range(3):
        # 바꾼걸 또 바꾸면 안됨.
        if row < col:
            arr[row][col], arr[col][row] =  arr[col][row], arr[row][col]