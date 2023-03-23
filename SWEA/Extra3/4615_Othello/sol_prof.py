import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())


    # 상하좌우 0으로 패딩
    arr = [[0] * 4 for _ in range(5)]
    print(arr)

    # i = N//2
    # arr[i][i] = arr[i-1][i-1] = 2
    # arr[i][i-1] = arr[i-1][i] = 1
    #
    # di = [-1, -1, 0, 1, 1, 1, 0, -1]
    # dj = [0, 1, 1, 1, 0, -1, -1, -1]
