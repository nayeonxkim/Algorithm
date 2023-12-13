import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

ans = [0] * N
for j in range(N):
    cnt = 0
    for i in range(N):
        if ans[i] == 0:
            cnt += 1
            if cnt > arr[j]:
                ans[i] = j+1
                break
print(*ans)
