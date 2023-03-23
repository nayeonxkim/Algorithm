import sys
sys.stdin = open('input.txt')

lst = list(range(1, 13))

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, 1<<12):
        subset = []
        for j in range(12):
            if i & (1<<j):
                subset.append(lst[j])
        if len(subset) == N and sum(subset) == K:
            ans += 1

    print(f'#{tc} {ans}')