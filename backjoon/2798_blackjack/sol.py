import sys
sys.stdin = open('input.txt')

from itertools import combinations
N, M = map(int, input().split())
cards = list(map(int, input().split()))

subset = list(combinations(cards, 3))
ans = []
for i in subset:
    if sum(i) <= M:
        ans.append(sum(i))
print(max(ans))
