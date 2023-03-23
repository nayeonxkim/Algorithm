import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    res = [0] * (N+1)
    for i in range(N):
        res[i+1] = res[i] + arr[i]

    maxV = -1000
    for i in range(N, 0, -1):
        for j in range(0, i):
            tot = res[i] - res[j]
            if maxV < tot:
                maxV = tot
    print(maxV)