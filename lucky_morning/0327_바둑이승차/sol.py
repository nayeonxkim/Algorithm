import sys
sys.stdin = open('input.txt')
from itertools import combinations

C, N = map(int, input().split())
lst = list(int(input()) for _ in range(N))
maxTot = 0

def DFS(i, tot, nowsum):
    global maxTot

    if tot + (sum(lst)-nowsum) < maxTot:
        return

    if tot > C:
        return

    if i >= N:
        maxTot = max(maxTot, tot)
        return


    DFS(i+1, tot+lst[i], nowsum+lst[i])
    DFS(i+1, tot, nowsum+lst[i])

DFS(0, 0, 0)
print(maxTot)

