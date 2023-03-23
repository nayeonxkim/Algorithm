import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input()))
    print(arr[i])

# 탐색 방향 제어
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

# 방문처리할 리스트, 1이면 방문했다.
visitied = [[0] * N for _ in range(N)]
# 방문한적 없고, 값이 1인 좌표 넣어줄 스택
stack = []



