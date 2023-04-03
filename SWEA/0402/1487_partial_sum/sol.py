import sys
sys.stdin = open('input.txt')

def backtrack(i, N, W, S):
    global cnt

    if S > W:
        return

    if i == N:
        if W == S:
            cnt += 1
        return

    backtrack(i+1, N, W, S+arr[i])
    backtrack(i+1, N, W, S)


T = int(input())
for tc in range(1, T+1):
    N, W = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    backtrack(0, N, W, 0)
    print(cnt)