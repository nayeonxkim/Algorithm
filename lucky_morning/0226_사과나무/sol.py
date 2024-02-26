import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

val = 0
k = -1
for i in range(N):
    if i <= N//2:
        k += 1
    else:
        k -= 1
    for j in range(N//2-k, N//2+k +1):
        val += arr[i][j]

print(val)