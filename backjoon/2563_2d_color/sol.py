import sys
sys.stdin = open('input.txt')

arr = [[0] * 100 for _ in range(100)]

N = int(input())
for n in range(N):
    A, B = map(int, input().split())
    for i in range(100-B, 90-B, -1):
        for j in range(A, A+10):
            arr[i][j] = 1

area = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            area += 1
print(area)