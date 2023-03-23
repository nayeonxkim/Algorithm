import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
res = [0] * (N+1)

for i in range(N):
    res[i+1] = res[i] + arr[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    ans = res[j] - res[i-1]
    print(ans)