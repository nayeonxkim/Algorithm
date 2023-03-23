# 전치행렬
N = 3
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f'기존 행렬: {arr}')

for row in range(N):
    for col in range(N):
        if row < col:
            arr[row][col], arr[col][row] = arr[col][row], arr[row][col]

print(f'전치 행렬 : {arr}')
print(f'{arr[0]}\n{arr[1]}\n{arr[2]}')