import sys
sys.stdin = open('input.txt')

# 1. 입력받음
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 2. 모든 치킨집, 집의 좌표 저장
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

# 3. backtrack 함수 정의
def backtrack(i, M, house, chicken, lst):

    global minV

    # 종료조건
    if i == len(chicken):
        return

    # 백트래킹
    if len(lst) == M:
        V = 0
        for h in house:
            hr, hc = h[0], h[1]
            minD = N * N
            for c in lst:
                cr, cc = c[0], c[1]
                D = abs(hr-cr) + abs(hc-cc)
                if minD >= D:
                    minD = D
            V += minD
        if minV >= V:
            minV = V
        return


    # 재귀호출
    backtrack(i+1, M, house, chicken, lst + [chicken[i]])
    backtrack(i+1, M, house, chicken, lst)

# 4. DFS 함수 호출
minV = 50 ** 3 * 2
backtrack(0, M, house, chicken, [])

# 5. 정답 출력
print(minV)