import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[0] * N for _ in range(N)]

    i = N//2
    arr[i][i] = arr[i-1][i-1] = 2
    arr[i][i-1] = arr[i-1][i] = 1

    di = [-1, -1, 0, 1, 1, 1, 0, -1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]


    for _ in range(M):
        i, j, color = map(int, input().split())
        row = i - 1
        col = j - 1

        arr[row][col] = color
        tlst = []
        for k in range(8):

            for n in range(1, N):
                ni = row + di[k] * n
                nj = col + dj[k] * n
                if 0 <= ni < N and 0 <= nj < N: # 범위내에서
                    if arr[ni][nj] == 0:    # 0이면 더이상 뻗어나가지 않고 멈춤
                        break
                # 나랑 다른 색의 돌이면 뒤집을 돌 후보에 추가한다.
                    elif arr[ni][nj] != color:
                        tlst.append((ni, nj))
                # 같은 돌이면, 후보를 뒤집는다.
                    else:
                        while tlst:
                            ti, tj = tlst.pop()
                            arr[ti][tj] = color
                        break



        bcnt = wcnt = 0
        for lst in arr:
            bcnt += lst.count(1)
            wcnt += lst.count(2)
        print(bcnt, wcnt)

        for i in range(N):
            print(arr[i])

        # if ni > row:
        #     r = ni - 1
        # elif ni < row:
        #     r = ni + 1
        # else:
        #     r = ni
        #
        # if nj > col:
        #     c = nj - 1
        # elif nj < col:
        #     c = nj + 1
        # else:
        #     c = nj
        #
        # arr[r][c] = color



