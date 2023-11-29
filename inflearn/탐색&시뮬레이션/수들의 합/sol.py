import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

# 1. 재귀 -> N이 10000까지도 돼서 recursion error남
# def check(i, sum):
#     global cnt
#
#     if sum == M:
#         cnt += 1
#         return
#
#     if i == N:
#         return
#
#     check(i+1, sum+A[i])
#
# for i in range(N):
#     check(i, 0)
# print(cnt)

# 2. 그냥 for문 두 개
for i in range(N):
    sum = A[i]
    for j in range(i+1, N):
        sum += A[j]
        if sum == M:
            cnt += 1
            break
print(cnt)