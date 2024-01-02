import sys
sys.stdin = open('input.txt')
from itertools import permutations

n = int(input())
k = int(input())

cards = [input() for _ in range(n)]
lst = list(permutations(cards, k))

ans = []
for l in lst:
    num = ''
    for n in l:
        num += n
    num = int(num)
    if num not in ans:
        ans.append(num)

print(len(ans))