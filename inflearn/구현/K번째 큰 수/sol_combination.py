import sys
sys.stdin = open('input.txt')

from itertools import combinations

# 1. 리스트
N, K = map(int, input().split())
cards = list(map(int, input().split()))

# 2. 3개씩 합의 집합 구하기
combi = combinations(cards, 3)
sum_lst = set(sum(lst) for lst in combi)

# 내림차순 정렬 및 K번째 큰 합 출력
res = list(sum_lst)
res.sort(reverse=True)
print(res[K-1])
