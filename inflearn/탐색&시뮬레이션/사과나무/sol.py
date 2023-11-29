import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


s = e = N//2
i = 0
sum = 0
for i in range(N):
    for j in range(s, e+1):
        sum += arr[i][j]

    if i < N // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(sum)