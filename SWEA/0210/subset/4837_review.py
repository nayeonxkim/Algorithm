import sys
sys.stdin = open('4837_input.txt')

A = list(range(1, 13))

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    res = 0
    for i in range(1, 1<<12):
        subset = []
        for j in range(12):
            if i & (1<<j):
                subset.append(A[j])

        if len(subset) == N and sum(subset) == K:
            res += 1

    print(f'#{tc} {res}')