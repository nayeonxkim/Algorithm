import sys
sys.stdin = open('input.txt')

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(arr)

# 15 이상

# 1개의 값
ans = 0
for n in arr:
    if n >= S:
        ans = 1

