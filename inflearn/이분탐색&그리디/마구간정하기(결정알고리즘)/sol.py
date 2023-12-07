import sys
sys.stdin = open('input.txt')

N, C = map(int, input().split())
arr = list(int(input()) for _ in range(N))

# 1. 마구간 정렬
arr.sort()

# 2.
start = 1
end = N-1

