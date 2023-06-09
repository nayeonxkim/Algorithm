import sys
sys.stdin = open('input.txt')

def backtrack(i, N, K, S):
    global cnt

    if S > K:
        return

    if i == N:
        if S == K:
            cnt += 1
        return

    backtrack(i+1, N, K, S + arr[i])
    backtrack(i+1, N, K, S)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    backtrack(0, N, K, 0)
    print(f'#{tc} {cnt}')
