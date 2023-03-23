import sys
sys.stdin = open('input.txt')
import copy
from itertools import combinations


def check(lst):

    for tp in lst:
        tmp[tp[0]][tp[1]] = 1

    for i in range(N):
        for j in range(M):





N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    print(arr[i])

di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]
visited = [[0] * M for _ in range(N)]
tmp = copy.deepcopy(arr)
# 벽을 놓을 수 있는 곳 찾기
queue = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if not arr[ni][nj] and not visited[ni][nj]:
                        queue.append((ni, nj))

# 세 군데씩 1을 놓아보면서,
# 2에서 0으로 이어진 곳은 모두 2로 바꾼다.
# 바뀐 arr에서 0의 개수를 센다.
# 0의 개수가 최대인 값을 출력한다.

wall_lst = list(combinations(queue, 3))
for lst in wall_lst:
    check(lst)
print(arr)