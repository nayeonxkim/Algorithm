import sys
sys.stdin = open('input.txt')

N = int(input())
lst = list(map(int, input().split()))
M = int(input())

minN = M
def backtrack(i, N, lst, M, V, n):
    global minN
    # 종료
    if i >= N:
        return
    # 가지치기1
    if V > M:
        return
    # 가지치기2
    if n > minN:
        return
    # 정답 로직
    if V == M:
        minN = min(minN, n)

    backtrack(i+1, N, lst, M, V+lst[i], n+1)
    backtrack(i, N, lst, M, V + lst[i], n+1)
    backtrack(i+1, N, lst, M, V, n)

backtrack(0, N, lst, M, 0, 0)
print(minN)