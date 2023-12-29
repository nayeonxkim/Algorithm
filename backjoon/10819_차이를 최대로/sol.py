import sys
sys.stdin = open('input.txt')
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

def backtrack(lst):
    i = 0
    res = 0
    while i < N-1:
        res += abs(lst[i] - lst[i+1])
        i += 1
    return res

P = list(permutations(A, N))
ans = 0
for lst in P:
    res = backtrack(lst)
    ans = max(ans, res)
print(ans)