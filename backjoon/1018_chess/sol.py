import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(list(input()) for _ in range(N))

def check_board(row, col):
    # 4방향 탐색 좌표
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    # 색칠해야하는 개수
    ans = 0

    # 8 * 8로 확인하며 색칠갯수 찾음
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            for t in range(4):

                ni = row + di[t]
                nj = col + dj[t]

                if 0 <= ni < N or 0 <= nj < M:
                    # 현재 색과 같다면 +1
                    if arr[row][col] == arr[ni][nj]:
                        ans += 1

                        if arr[ni][nj] == 'B':
                            arr[ni][nj] = 'W'
                        else:
                            arr[ni][nj] = 'B'


                        # 최소값을 넘으면 바로 종료
                        if ans >= minA:
                            return ans

    return ans
                

minA = N * M
print(minA)

for row in range(0, N - 8):
    for col in range(0, M - 8):
        ans = check_board(row, col)
        print(ans)
        if minA >= ans:
            minA = ans

print(minA)