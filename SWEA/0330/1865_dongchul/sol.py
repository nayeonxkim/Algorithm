'''
행 인덱스 = 직원 번호
열 인덱스 = 작업 번호

N*N 배열에서 N개의 곱이 최대인 값
같은 행, 같은 열에 1이 두개 있으면 안된다.

assign
[ 1 0 0 ]
[ 0 0 0 ]
[ 0 0 0 ]
1을 놓는 모든 경우의 수
근데 같은 행열X
'''


import sys
sys.stdin = open('input.txt')

def promising(i, j):
    # 위에 있으면 X
    ni = i - 1
    while 0 <= ni < N:
        if assign[ni][j]:
            return 0
        ni -= 1

    return 1


def BackTrack(i, N):
    # 모든 작업에 대해 조사 끝나면 종료
    global cnt
    global maxV

    if i == N:
        stack = []
        for r in range(N):
            for c in range(N):
                if assign[r][c]==1:
                    stack.append((r, c))


        ans = 0
        while stack:
            row, col = stack.pop()
            ans *= arr[row][col]/100
        ans *= 100

        if maxV < ans:
            maxV = ans

        return ans

    else:
        for j in range(N):
            if promising(i, j):
                assign[i][j] = 1
                BackTrack(i+1, N)
                assign[i][j] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    assign = [[0]*N for _ in range(N)]
    # 0행부터, 행별로 한개씩해서 N개 까지 조사
    cnt = 0
    maxV = 0
    # BackTrack(0, N)
    print(BackTrack(0, N))
