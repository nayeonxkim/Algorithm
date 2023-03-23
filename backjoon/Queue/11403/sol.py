import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    print(arr[i])