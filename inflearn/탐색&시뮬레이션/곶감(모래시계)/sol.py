import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

# 1. 회전
for _ in range(M):
    r, d, n = map(int, input().split())

    if d == 0:
        for _ in range(n):
            arr[r-1].append(arr[r-1].pop(0))
    else:
        for _ in range(n):
            arr[r-1].insert(0, arr[r-1].pop())

# 2. 곶감 합계
s = 0
e = N-1
sum = 0
for i in range(N):
    for j in range(s, e+1):
        sum += arr[i][j]
    if i < N//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(sum)