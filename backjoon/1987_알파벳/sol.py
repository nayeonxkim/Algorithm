import sys
sys.stdin = open('input.txt')
from collections import deque

'''
- 상하좌우 중 간적 없는 알파벳일 때만 갈 수 있음
- 호출될 때 cnt + 1, cnt의 최대값 구해야함

'''

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]



def DFS(arr):

    visited = [arr[0][0]]
    stack = deque()
    stack.append((0, 0))
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]


    while stack:
        i, j = stack.pop()

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < R and 0 <= nj < C:
                if arr[ni][nj] not in visited:
                    visited.append(arr[ni][nj])
                    stack.append((ni, nj))



# DFS(arr, [arr[0][0]], 1)
print([arr[0][0]]+ [arr[1][1]])