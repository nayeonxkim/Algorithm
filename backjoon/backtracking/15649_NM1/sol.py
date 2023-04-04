import sys
sys.stdin = open('input.txt')

def backtrack(i, arr, M, lst):

    if len(lst) == M:
        print(*lst)
        return

    visited[i] = 1
    for n in range(N):
        if not visited[n]:
            backtrack(n, arr, M, lst + [arr[i]])
    visited[i] = 0


N, M = map(int, input().split())
arr = list(range(1, N+1))
# [1, 2, 3, 4]
visited = [0] * N
print(arr)
# 0행부터
backtrack(0, arr, M, [])