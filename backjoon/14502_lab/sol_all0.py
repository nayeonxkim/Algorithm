import sys
sys.stdin = open('input.txt')
from itertools import combinations
import copy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# 값이 0인 좌표들을 세 개씩 조합을 만든다.
# 이 세 좌표의 조합들이 벽이 들어갈 후보군이 된다.
zeros = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zeros.append((i, j))
candidates = list(combinations(zeros, 3))

# 후보군을 차례대로 순회하면서 벽을 세 개씩 세우고,
# 벽을 세운 후에 바이러스가 모두 퍼진 상태를 만들어낸다.
# 벽에 의해 바이러스가 퍼지지 않은 방(0)의 개수를 센다.

# 바이러스가 퍼진다 = 2와 인접한 0들(1에 의해 막혀있지 않은 모든 0)에 대해 infected = 1

# 2와 인접한 것을 판단할 4방향
di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]

# 모든 후보군에서, 감염되지 않은 안전지역의 최대 수
max_cnt = 0

## 1. candidates에서 세트 하나를 뽑아서 해당 세트에 있는 세 좌표의 값을 1로 만든다. : 벽을 세운다.
for lst in candidates:
    cnt = 0
    tmp = copy.deepcopy(arr)
    infected = [[0] * M for _ in range(N)]
    for p in lst:
        tmp[p[0]][p[1]] = 1

    ## 2. 완성된 tmp에서 작업 : 1로 막힐 때까지 0인 방을 감염시킨다.
    ## 2인 값을 찾아서 큐에 넣고, infected 표시한다.
    queue = []
    for i in range(N):
        for j in range(M):
            # 출발점은 2여야하고, 2는 여러개가 있기 때문에
            # 값이 2이면서 이전에 출발점으로 삼은적이 없는 2의 좌표를 출발점으로 한다.
            # 갈 수 있는 지점은 인큐하고 감염표시
            if tmp[i][j] == 2 and not infected[i][j]:
                queue.append((i, j))
                infected[i][j] = 1

                # 큐에 값이 없으면 새로운 출발점 찾으러 감.
                # 이어진 0이 없으면 해당 영역은 끝
                while queue:
                    # 디큐 해서 현재 위치 설정
                    row, col = queue.pop(0)

                    # 현재 위치에서 4방향 탐색하여
                    for k in range(4):
                        ni = row + di[k]
                        nj = col + dj[k]
                        # 배열을 벗어나지 않는 좌표일 때,
                        if 0 <= ni < N and 0 <= nj < M:
                            # 값이 0이고, 감염되지 않았으면
                            if tmp[ni][nj] == 0 and not infected[ni][nj]:
                                # 좌표를 인큐하고 감염 표시
                                queue.append((ni, nj))
                                infected[ni][nj] = 1

    ## 3. 감염이 끝난 배열에서 감염되지 않은 방의 개수를 센다.
    for i in range(N):
        for j in range(M):
            if infected[i][j] == 0 and tmp[i][j] == 0:
                cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)
