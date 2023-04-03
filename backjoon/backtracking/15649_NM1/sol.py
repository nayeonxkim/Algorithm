def backtrack(i, N, M, lst):



N, M = map(int, input().split())
arr = list(range(1, N+1))
# [1, 2, 3, 4]
visited = [0] * N
backtrack(0, N, M, [])
# 0행부터
