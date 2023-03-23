import sys
sys.stdin = open('input.txt')


def p(i, K, res):
    global chosen, ans

    if i == K:
        lst.append(res)
        return
    
    for j in range(N):
        if chosen[j]:
            chosen[j] = 0
            p(i+1, K, res + [arr[i][j]])
            chosen[j] = 1

N = int(input())
arr = [0] * N

chosen = [0] * N
ans = []
for i in range(N):
    arr[i] = list(map(int, input().split()))


    p(i, N, [])
