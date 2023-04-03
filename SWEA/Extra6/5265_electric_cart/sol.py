import sys
sys.stdin = open('input.txt')

# 처음 행 = 0, 마지막 열 = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

