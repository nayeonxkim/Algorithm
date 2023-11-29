import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = int(input())

# 1. 회전
for _ in range(M):
    r, d, n = map(int, input().split())
    
