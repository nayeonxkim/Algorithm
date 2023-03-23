import sys
sys.stdin = open('input.txt')


N = int(input())

arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input()))
    print(arr[i])

# 탐색 방향 제어
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

# 방문처리할 리스트, 1이면 방문했다.
visitied = [[0] * N for _ in range(N)]
# 방문한적 없고, 값이 1인 좌표 넣어줄 스택
stack = []

## 단지의 시작점 찾기
# 배열 다 돌면서 방문한 적 없고, 값이 1인 좌표를 스택에 넣어준다.
# 시작점만 찾을 거라서 하나 찾으면 스택에 담고 더 찾지 않음.
for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and visitied[i][j] == 0:
                stack.append((i, j))

# 단지에 몇 세대 있는지 담아줄 변수
cnt = 0

# 스택에 값이 있을 때까지 반복
while stack:
    # 현재 위치 좌표값 = stack의 top
    row, col = stack.pop()

    # 4방향 탐색하면서
    for k in range(4):
        ni = row + di[k]
        nj = col + dj[k]
        # 배열을 벗어나지 않고,
        if 0 <= ni < N and 0 <= nj < N:
            # 값이 1이고 방문한적 없는 곳을
            if arr[ni][nj] == 1 and visitied[ni][nj] == 0:
                # 방문기록 찍어주고, stack에 담아서 다음 이동좌표로 쓸 수 있게함.
                visitied[ni][nj] = 1
                stack.append((ni, nj))
                # 하나 찾았으니 세대수 +1
                cnt += 1

print(cnt)