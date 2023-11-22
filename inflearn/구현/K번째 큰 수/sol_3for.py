import sys
sys.stdin = open('input.txt')

# 1. 리스트 내림차순 정렬
N, K = map(int, input().split())
cards = list(map(int, input().split()))

# 2. 3개씩 합의 집합 구하기
res = set()
for i in range(N):
    for j in range(i+1, N):
        for l in range(j+1, N):
            res.add(cards[i] + cards[j] + cards[l])

# 내림차순 정렬 및 K번째 큰 합 출력
res = list(res)
res.sort(reverse=True)

print(res[K-1])