import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [0] * N
for n in range(N):
    arr[n] = int(input())

for i in range(N-1):
