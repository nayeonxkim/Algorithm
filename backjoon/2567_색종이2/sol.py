import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [[0] * 100 for _ in range(100)]
for _ in range(N):
    left, under = map(int, input().split())
    for i in range(99-under, 99-under-10, -1):
        for j in range(left, left+10):
            arr[i][j] = 1


di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt = 0
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1:
                    cnt += 1
            if cnt == 3:
                ans += 1
            elif cnt == 2:
                ans += 2
print(ans)
