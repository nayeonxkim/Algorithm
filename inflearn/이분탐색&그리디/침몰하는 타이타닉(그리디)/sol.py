from itertools import permutations
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
print(arr)

tot = 0
ppl = 0
i = 0
cnt = 0
while i < N:
    tot += arr[i]
    ppl += 1
    if tot > M or ppl > 2:
        cnt += 1
        tot = 0
    else:
        i += 1
print(cnt)