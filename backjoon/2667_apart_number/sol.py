import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input()))
    # print(arr[i]) # arr잘 받아왔나 확인

# arr랑 같은 모양으로 방문기록할 배열 만들어줌.
visited = [[0] * N for _ in range(N)]
stack = []

#  상 하 좌 우 좌표값
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
cnt = 0 # 얘는 몇 단지 있는지 세는 변수로 만들어써

res = []
# 상하좌우 확인해서 1이고 방문한 적 없으면 해당 지점을 스택에 넣는다.

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            # 방문했으니까 stack에 쌓고 visited 1로 바꿔
            stack.append((i, j))
            visited[i][j] = 1


            # 각 단지의 아파트 수
            cnt_per = 0
            # 스택에 값이 있을때까진 계속 반복
            while stack:
                # 스택 top을 현재 위치로 잡는다.
                row, col = stack.pop()

                # 현재 위치에서 상하좌우 탐색해서
                for k in range(4):
                    ni = row + di[k]
                    nj = col + dj[k]
                # 배열의 범위 내에서,
                    if 0 <= ni < N and 0 <= nj < N:
                    # 값이 1이고 방문한적 없는 지점을 찾는다.
                        if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    # 해당 지점을 스택에 push하고 방문기록을 남긴다.
                            stack.append((ni, nj))
                            visited[ni][nj] = 1
                    # 하나 찾았으니까 count 1 더해준다.
                            cnt_per += 1
        # 그럼 짜잔~ !
            res.append(cnt_per)

print(res) # cnt_per에 첫 시작점이 반영되지 않음 -> +1해서 출력
