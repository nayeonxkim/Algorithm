import sys
sys.stdin = open('input.txt')
from itertools import combinations

num, N = map(int, input().split())
num = str(num)
ans = ('').join(max(list(combinations(num, len(num)-N))))
print(int(ans))
