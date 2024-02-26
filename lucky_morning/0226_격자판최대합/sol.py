import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


# 행의 합
maxV = 0
for i in range(N):
    val = 0
    for j in range(N):
        val += arr[i][j]
    maxV = max(maxV, val)

# 대각선의 합
val = 0
for i in range(N):
    val += arr[i][i]
maxV = max(maxV, val)

val = 0
for i in range(N):
    val += arr[i][N-i-1]
maxV = max(maxV, val)

# 열의 합
for i in range(N):
    val = 0
    for j in range(N):
        val += arr[j][i]
    maxV = max(maxV, val)

# 최대값 출력
print(maxV)