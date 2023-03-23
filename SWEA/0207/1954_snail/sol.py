'''

3
range(3)

'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    start = 0
    end = N

    while start <= N and 0 <= end:
        for j in range(start, end):
            arr[start][j] += j + 1

        for i in range(start + 1, end):
            arr[i][end-1] = arr[start][end-1] + i

        for j in range(end-2, start-1, -1):
            arr[N-1][j] = arr[end-1][end-1] + (end - 1 - j)

        for i in range(end-2, start, -1):
            arr[i][start] = arr[end-1][start] + (end - 1 - i)

        start += 1
        end -= 1


        for i in range(N):
            if 0 not in arr[i]:
                break

    for l in range(N):
        print(arr[l])
    print('========================')