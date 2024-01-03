import sys
sys.stdin = open('input.txt')

R, C = map(int, input().split())
arr = [input() for _ in range(R)]

max_cnt = 0
def DFS(i, j, arr, visited, cnt):

    # 2. max_cnt 업데이트
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    # 1. 4방향 탐색 -> 방문한적 없는 알파벳이면 그 위치에서 다시 탐색
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < R and 0 <= nj < C:
            if arr[ni][nj] not in visited:
                DFS(ni, nj, arr, visited+[arr[ni][nj]], cnt + 1)

# 3. 첫 시작점 = 왼쪽 상단
DFS(0, 0, arr, [arr[0][0]], 1)

print(max_cnt)