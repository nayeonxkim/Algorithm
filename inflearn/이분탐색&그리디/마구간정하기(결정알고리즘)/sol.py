import sys
sys.stdin = open('input.txt')

N, C = map(int, input().split())
arr = list(int(input()) for _ in range(N))

# 1. 마구간 정렬
for n in range(N-1, -1, -1):
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)

# 2.