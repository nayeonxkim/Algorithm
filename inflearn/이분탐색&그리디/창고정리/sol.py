import sys
sys.stdin = open('input.txt')

L = int(input())
arr = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    maxidx = arr.index(max(arr))
    minidx = arr.index(min(arr))
    arr[maxidx] -= 1
    arr[minidx] += 1
print(max(arr) - min(arr))