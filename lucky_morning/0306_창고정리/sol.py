import sys
sys.stdin = open('input.txt')

L = int(input())
lst = list(map(int, input().split()))
M = int(input())

# 1. 정렬
lst.sort()

# 2. 최대 - 1, 최소 + 1 -> 재정렬
for _ in range(M):
    lst[0] += 1
    lst[-1] -= 1
    lst.sort()

print(lst[-1] - lst[0])