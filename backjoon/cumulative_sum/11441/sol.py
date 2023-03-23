import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = [0] * (N+1)

for i in range(N):
    res[i+1] = res[i] + arr[i]

M = int(sys.stdin.readline())
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    ans = res[B] - res[A-1]
    print(ans)