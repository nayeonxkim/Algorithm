import sys
sys.stdin = open('input.txt')

from collections import Counter

N, M = map(int, input().split())

# 1. 합 리스트
sum_list = []
for n in range(1, N+1):
    for m in range(1, M+1):
        sum_list.append(n + m)

# 2. 각 합이 몇 번 나왔는지
count = Counter(sum_list)
max_cnt = max(count.values())
res = [k for k, v in count.items() if v == max_cnt]
print(*res)


