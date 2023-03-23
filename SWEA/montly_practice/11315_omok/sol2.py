import sys
sys.stdin = open('input.txt')

def find_o(arr):
    stack = []

    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o' and not visited[i][j]:
                stack.append((i, j))
                visited[i][j] = 1


                while stack:

                    row, col = stack.pop()

                    for k in range(8):
                        ni = row + di[k]
                        nj = col + dj[k]

                        point = 0
                        if 0 <= ni < N and 0 <= nj < N:
                            while arr[ni][nj] == 'o' and not visited[ni][nj]:
                                point += 1
                                stack.append((ni, nj))
                                visited[ni][nj] = 1
                                if point == 5:
                                    return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    
    ans = find_o(arr)
    print(ans)
