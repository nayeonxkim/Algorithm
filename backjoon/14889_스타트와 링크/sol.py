import sys
sys.stdin = open('input.txt')
from itertools import combinations

N = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(N)]
teams = list(combinations(range(N), N // 2))

# 점수 계산 함수
def score(team, N):
    score = 0
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            x, y = team[i], team[j]
            score += arr[x][y]
            score += arr[y][x]
    return score

minD = 100
# 스타트팀 점수 구하기
for team in teams:

    visited = [0] * N

    # 스타트팀
    for i in team:
        visited[i] = 1
    start = score(team, N)

    # 링크팀
    link_team = []
    for i in range(N):
        if visited[i] != 1:
            link_team.append(i)
    link = score(link_team, N)

    minD = min(minD, abs(start-link))

print(minD)
