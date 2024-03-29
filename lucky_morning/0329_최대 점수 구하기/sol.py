import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

maxPoint = 0
def DFS(i, point, time):
    global maxPoint

    if time > M:
        return

    if i >= N:
        if time <= M:
            maxPoint = max(maxPoint, point)
            return

    DFS(i+1, point+lst[i][0], time+lst[i][1])
    DFS(i+1, point, time)

DFS(0, 0, 0)
print(maxPoint)